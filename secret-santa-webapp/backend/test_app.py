"""Run: python test_app.py"""
from app import app, create_secret_santa_list, parse_participants
from card_templates import THEMES, render_card


def test_pairing():
    names = list('ABCDE')
    excl = {'A': ['B'], 'B': ['A']}
    for _ in range(200):
        pairs = create_secret_santa_list(names, excl)
        assert sorted(r for _, r in pairs) == names
        assert all(g != r and r not in excl.get(g, []) for g, r in pairs)
    try:
        create_secret_santa_list(['A', 'B', 'C'], {'A': ['B', 'C']})
        raise AssertionError('expected ValueError')
    except ValueError:
        pass


def test_validation():
    ok = [{'name': n, 'email': f'{n}@x.com'} for n in 'ABC']
    assert len(parse_participants(ok, True)) == 3
    for bad in (ok[:2], ok + [ok[0]], [{'name': 'A'}] + ok[1:]):
        try:
            parse_participants(bad, True)
            raise AssertionError('expected ValueError')
        except ValueError:
            pass


def test_cards():
    giver = {'name': '<b>Gi</b>'}
    rec = {'name': 'Re', 'interests': '<script>alert(1)</script>', 'address': '1 Main'}
    for key in THEMES:
        html = render_card(key, giver, rec, 'Hi {giver_name}, buy for {recipient_name}')
        assert '<script>' not in html and '<b>Gi' not in html
        assert 'Hi &lt;b&gt;Gi&lt;/b&gt;, buy for Re' in html
        assert '{giver}' not in html and '1 Main' in html


def test_api():
    c = app.test_client()
    assert len(c.get('/api/themes').json) == len(THEMES)
    people = [{'name': n, 'email': f'{n}@x.com', 'interests': 'x'} for n in 'ABC']
    r = c.post('/api/send', json={'participants': people, 'testMode': True, 'emailTemplate': 'hi'})
    assert r.status_code == 200 and len(r.json['pairings']) == 3 and 'html' in r.json['pairings'][0]
    r = c.post('/api/send', json={'participants': people, 'testMode': True,
                                  'exclusions': {'A': ['B', 'C']}})
    assert r.status_code == 400
    r = c.post('/api/send', json={'participants': people})  # real send, no SMTP creds
    assert r.status_code == 400


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
    print('ok')

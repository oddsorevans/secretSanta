"""Email card themes. One email-safe layout, themed by tokens.

Gmail strips position/transform and most gradients, so every themed area has a
solid bgcolor fallback; gradients/stripes are progressive enhancement.
"""
from datetime import datetime
from html import escape

DEFAULT_THEME = 'dossier'

THEMES = {
    'dossier': {
        'name': 'Top Secret Dossier',
        'description': 'Manila folder, typewriter text, redaction bars',
        'emoji': '🕵️',
        'page': '#d9d2c3', 'card': '#f1e3b8', 'edge': '#8c7a4e',
        'head_bg': '#e6d49b', 'head_fg': '#1c1c1c',
        'font': "'Courier New', Courier, monospace", 'heading_font': "'Courier New', Courier, monospace",
        'kicker': 'CLASSIFIED // EYES ONLY', 'title': 'OPERATION SECRET SANTA',
        'greeting': 'AGENT {giver},', 'label': 'YOUR TARGET',
        'interests_label': 'KNOWN INTERESTS', 'address_label': 'LAST KNOWN ADDRESS',
        'accent': '#b3001b', 'body_fg': '#2a2a2a', 'panel': '#fbf3d9',
        'box_bg': '#1c1c1c', 'box_fg': '#f1e3b8', 'box_label': '#ff5a5a',
        'footer': 'This message will not self-destruct. Please keep it secret anyway.',
        'stripe': 'repeating-linear-gradient(90deg,#1c1c1c 0 38px,#f1e3b8 38px 46px)', 'stripe_bg': '#1c1c1c',
    },
    'northpole_post': {
        'name': 'North Pole Post',
        'description': 'Vintage airmail with striped border and postmark',
        'emoji': '✉️',
        'page': '#e9e4d8', 'card': '#fffaf0', 'edge': '#c8102e',
        'head_bg': '#fffaf0', 'head_fg': '#14325c',
        'font': "Georgia, 'Times New Roman', serif", 'heading_font': "Georgia, 'Times New Roman', serif",
        'kicker': 'PAR AVION · AIR MAIL · NORTH POLE', 'title': 'Secret Santa Special Delivery',
        'greeting': 'Dear {giver},', 'label': 'Deliver your gift to',
        'interests_label': 'Return address tastes', 'address_label': 'Mail it to',
        'accent': '#c8102e', 'body_fg': '#26344d', 'panel': '#f6efe0',
        'box_bg': '#14325c', 'box_fg': '#fffaf0', 'box_label': '#f4c7cd',
        'footer': 'Postmarked at the North Pole · Handle with festive care',
        'stripe': 'repeating-linear-gradient(135deg,#c8102e 0 18px,#fffaf0 18px 30px,#14325c 30px 48px,#fffaf0 48px 60px)', 'stripe_bg': '#c8102e',
    },
    'aurora': {
        'name': 'Midnight Aurora',
        'description': 'Deep navy night sky with teal and violet glow',
        'emoji': '🌌',
        'page': '#0a0f24', 'card': '#121a3a', 'edge': '#2f3e7a',
        'head_bg': '#1b6f7a', 'head_fg': '#f4fbff',
        'font': "'Helvetica Neue', Arial, sans-serif", 'heading_font': "'Trebuchet MS', 'Helvetica Neue', Arial, sans-serif",
        'kicker': '✦ · ˚ ✧ · ✦', 'title': 'Secret Santa',
        'greeting': 'Hello, {giver}', 'label': 'Under the northern lights, you are gifting',
        'interests_label': 'They glow for', 'address_label': 'Find them at',
        'accent': '#7ef0d8', 'body_fg': '#d6def7', 'panel': '#1a2450',
        'box_bg': '#3a2a7a', 'box_fg': '#f4fbff', 'box_label': '#a9f5e6',
        'footer': 'Keep the secret — the sky is watching ✦',
        'stripe': 'linear-gradient(90deg,#1de9b6,#5b8cff,#a24bff)', 'stripe_bg': '#5b8cff',
        'head_grad': 'linear-gradient(135deg,#0f8a8f 0%,#4a3fb0 60%,#7a2fb8 100%)',
    },
    'ski_lodge': {
        'name': 'Retro Ski Lodge',
        'description': '70s poster stripes in burnt orange and mustard',
        'emoji': '🎿',
        'page': '#f3e6cc', 'card': '#fbf1dc', 'edge': '#7a3b10',
        'head_bg': '#c8561b', 'head_fg': '#fbf1dc',
        'font': "'Trebuchet MS', Verdana, sans-serif", 'heading_font': "Georgia, 'Times New Roman', serif",
        'kicker': 'EST. 1974 · APRÈS-SKI SOCIAL CLUB', 'title': 'Secret Santa Lodge Party',
        'greeting': 'Welcome in, {giver}!', 'label': 'You are shredding gifts for',
        'interests_label': 'On their wish list', 'address_label': 'Send the loot to',
        'accent': '#c8561b', 'body_fg': '#4a2a12', 'panel': '#f4e3bf',
        'box_bg': '#e8a317', 'box_fg': '#3b1f0b', 'box_label': '#7a3b10',
        'footer': 'Hot cocoa required · Spoilers are a black diamond offense',
        'stripe': 'linear-gradient(180deg,#7a3b10 0 25%,#c8561b 25% 50%,#e8a317 50% 75%,#f3e6cc 75% 100%)', 'stripe_bg': '#c8561b',
    },
    'gingerbread': {
        'name': 'Gingerbread Lane',
        'description': 'Cookie brown with icing borders and candy accents',
        'emoji': '🍪',
        'page': '#f6e9dc', 'card': '#a8683a', 'edge': '#ffffff',
        'head_bg': '#8a4f26', 'head_fg': '#fff8ef',
        'font': "'Trebuchet MS', 'Comic Sans MS', sans-serif", 'heading_font': "'Trebuchet MS', 'Comic Sans MS', sans-serif",
        'kicker': '🍬 · 🍪 · 🍬 · 🍪 · 🍬', 'title': 'Gingerbread Secret Santa',
        'greeting': 'Hi {giver}!', 'label': "You're baking up a gift for",
        'interests_label': 'Their sweet spots', 'address_label': 'Deliver the treats to',
        'accent': '#d6283f', 'body_fg': '#4a2a14', 'panel': '#fff8ef',
        'box_bg': '#fff8ef', 'box_fg': '#4a2a14', 'box_label': '#d6283f',
        'footer': "Mum's the word — don't crumble under pressure! 🍪",
        'stripe': 'repeating-linear-gradient(90deg,#ffffff 0 14px,#8a4f26 14px 22px)', 'stripe_bg': '#ffffff',
        'greet': '#fff8ef',
    },
}


def theme_list():
    return [
        {'key': k, 'name': t['name'], 'description': t['description'], 'emoji': t['emoji']}
        for k, t in THEMES.items()
    ]


def fill_template(template, giver, recipient):
    """Substitute {giver_name} etc. (plain text, unescaped)."""
    return (template
            .replace('{giver_name}', giver['name'])
            .replace('{recipient_name}', recipient['name'])
            .replace('{recipient_interests}', recipient.get('interests', ''))
            .replace('{recipient_address}', recipient.get('address', '')))


def render_card(theme_key, giver, recipient, message_template):
    """Return the full HTML email. All user-supplied text is escaped."""
    t = THEMES.get(theme_key, THEMES[DEFAULT_THEME])
    e = escape
    message = e(fill_template(message_template, giver, recipient))
    greeting = e(t['greeting']).replace('{giver}', e(giver['name']))
    year = datetime.now().year

    def grad(bg, css=None):
        # solid bgcolor for clients that drop gradients, css gradient on top
        return f'bgcolor="{bg}" style="background-color:{bg};' + (f'background-image:{css};' if css else '')

    address = ''
    if recipient.get('address'):
        address = f'''
              <p style="margin:18px 0 4px;color:{t['box_label']};font-size:12px;letter-spacing:2px;text-transform:uppercase;">{e(t['address_label'])}</p>
              <p style="margin:0;color:{t['box_fg']};font-size:16px;line-height:1.5;">{e(recipient['address'])}</p>'''

    return f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background-color:{t['page']};font-family:{t['font']};">
<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{t['page']}" style="padding:32px 12px;"><tr><td align="center">
  <table width="600" cellpadding="0" cellspacing="0" bgcolor="{t['card']}" style="max-width:600px;width:100%;background-color:{t['card']};border:4px solid {t['edge']};border-radius:6px;">
    <tr><td height="16" {grad(t['stripe_bg'], t['stripe'])}font-size:0;line-height:16px;">&nbsp;</td></tr>
    <tr><td align="center" {grad(t['head_bg'], t.get('head_grad'))}padding:32px 24px;">
      <p style="margin:0 0 10px;color:{t['head_fg']};font-size:12px;letter-spacing:3px;opacity:.85;">{e(t['kicker'])}</p>
      <h1 style="margin:0;color:{t['head_fg']};font-family:{t['heading_font']};font-size:32px;line-height:1.2;">{e(t['title'])}</h1>
      <p style="margin:10px 0 0;color:{t['head_fg']};font-size:14px;letter-spacing:4px;">{year}</p>
    </td></tr>
    <tr><td style="padding:28px 32px 8px;">
      <h2 style="margin:0 0 16px;color:{t.get('greet', t['accent'])};font-family:{t['heading_font']};font-size:24px;">{greeting}</h2>
      <div bgcolor="{t['panel']}" style="background-color:{t['panel']};border-left:5px solid {t['accent']};border-radius:4px;padding:20px;">
        <p style="margin:0;color:{t['body_fg']};font-size:15px;line-height:1.7;white-space:pre-wrap;">{message}</p>
      </div>
    </td></tr>
    <tr><td style="padding:16px 32px 32px;">
      <div bgcolor="{t['box_bg']}" style="background-color:{t['box_bg']};border-radius:6px;padding:26px;text-align:center;">
        <p style="margin:0 0 8px;color:{t['box_label']};font-size:12px;letter-spacing:2px;text-transform:uppercase;">{e(t['label'])}</p>
        <h3 style="margin:0;color:{t['box_fg']};font-family:{t['heading_font']};font-size:34px;line-height:1.2;">{e(recipient['name'])}</h3>
        <p style="margin:18px 0 4px;color:{t['box_label']};font-size:12px;letter-spacing:2px;text-transform:uppercase;">{e(t['interests_label'])}</p>
        <p style="margin:0;color:{t['box_fg']};font-size:16px;line-height:1.5;font-style:italic;">{e(recipient.get('interests', ''))}</p>{address}
      </div>
    </td></tr>
    <tr><td align="center" {grad(t['head_bg'], t.get('head_grad'))}padding:18px 24px;">
      <p style="margin:0;color:{t['head_fg']};font-size:13px;">{e(t['footer'])}</p>
    </td></tr>
    <tr><td height="16" {grad(t['stripe_bg'], t['stripe'])}font-size:0;line-height:16px;">&nbsp;</td></tr>
  </table>
</td></tr></table>
</body>
</html>'''

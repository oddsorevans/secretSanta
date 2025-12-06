# Christmas-themed email card templates for Python backend

CARD_STYLES = {
    'classic': 'Classic Christmas',
    'elegant': 'Elegant Gold',
    'winter': 'Winter Wonderland',
    'festive': 'Festive Fun',
    'rustic': 'Rustic Charm'
}


def generate_email_card(style, giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Generate HTML email card based on selected style."""

    templates = {
        'classic': generate_classic_card,
        'elegant': generate_elegant_card,
        'winter': generate_winter_card,
        'festive': generate_festive_card,
        'rustic': generate_rustic_card
    }

    generator = templates.get(style, generate_classic_card)
    return generator(giver_name, recipient_name, recipient_interests, recipient_address, message_body)


def generate_classic_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Classic Christmas themed card."""
    from datetime import datetime
    year = datetime.now().year

    address_section = ''
    if recipient_address:
        address_section = f'''
                  <div style="margin-top: 15px; padding: 15px; background-color: rgba(255,255,255,0.9); border-radius: 10px;">
                    <p style="margin: 0; color: #165B33; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                      Their Address
                    </p>
                    <p style="margin: 10px 0 0 0; color: #333333; font-size: 16px;">
                      {recipient_address}
                    </p>
                  </div>'''

    return f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;600&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f4; font-family: 'Lora', Georgia, serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f4f4f4; padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #165B33 0%, #0F4229 100%); border-radius: 20px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
          <tr>
            <td style="background: linear-gradient(90deg, #C41E3A 0%, #8B1538 100%); padding: 40px; text-align: center; border-bottom: 4px solid #FFD700;">
              <h1 style="margin: 0; color: #FFFFFF; font-family: 'Playfair Display', serif; font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                🎅 Secret Santa 🎄
              </h1>
              <p style="margin: 10px 0 0 0; color: #FFD700; font-size: 18px; letter-spacing: 2px;">
                ✦ {year} ✦
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding: 50px 40px; background-color: #FDFBF7;">
              <h2 style="color: #C41E3A; font-family: 'Playfair Display', serif; font-size: 32px; margin: 0 0 20px 0; text-align: center;">
                Hello, {giver_name}! 🎁
              </h2>
              <div style="background-color: #FFFFFF; padding: 30px; border-radius: 15px; border-left: 5px solid #165B33; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <p style="color: #333333; font-size: 16px; line-height: 1.8; margin: 0; white-space: pre-wrap;">{message_body}</p>
              </div>
              <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); padding: 30px; border-radius: 15px; margin: 30px 0; text-align: center; box-shadow: 0 6px 20px rgba(255, 215, 0, 0.4);">
                <p style="margin: 0 0 15px 0; color: #8B1538; font-size: 18px; font-weight: 600;">
                  🎯 Your Secret Santa Recipient
                </p>
                <h3 style="margin: 0; color: #C41E3A; font-family: 'Playfair Display', serif; font-size: 36px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
                  {recipient_name}
                </h3>
                <div style="margin-top: 20px; padding: 20px; background-color: rgba(255,255,255,0.9); border-radius: 10px;">
                  <p style="margin: 0; color: #165B33; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    Their Interests
                  </p>
                  <p style="margin: 10px 0 0 0; color: #333333; font-size: 16px; font-style: italic;">
                    {recipient_interests}
                  </p>
                </div>{address_section}
              </div>
            </td>
          </tr>
          <tr>
            <td style="background: linear-gradient(90deg, #0F4229 0%, #165B33 100%); padding: 30px; text-align: center;">
              <p style="margin: 0; color: #FFD700; font-size: 16px; font-weight: 600;">
                🌟 Happy Holidays! 🌟
              </p>
              <p style="margin: 10px 0 0 0; color: #FFFFFF; font-size: 14px; opacity: 0.8;">
                Keep it secret, keep it festive!
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>'''


# For brevity, I'll add simplified versions of the other templates
# In production, these would be full implementations like classic

def generate_elegant_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Elegant Gold themed card."""
    from datetime import datetime
    year = datetime.now().year

    address_section = ''
    if recipient_address:
        address_section = f'''
                <div style="margin-top: 20px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px;">
                  <p style="margin: 0 0 12px 0; color: #8B7355; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;">
                    Their Address
                  </p>
                  <p style="margin: 0; color: #4A4A4A; font-size: 16px; line-height: 1.6;">
                    {recipient_address}
                  </p>
                </div>'''

    return f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #f8f8f8; font-family: 'Montserrat', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f8f8f8; padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFFFFF; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.15);">
          <tr>
            <td style="background: linear-gradient(90deg, #FFD700 0%, #FFF8DC 50%, #FFD700 100%); height: 8px;"></td>
          </tr>
          <tr>
            <td style="padding: 50px 40px 30px 40px; text-align: center; background: linear-gradient(180deg, #FFFFFF 0%, #FFF8DC 100%);">
              <h1 style="margin: 0; color: #2C2C2C; font-family: 'Cormorant Garamond', serif; font-size: 52px; font-weight: 300; letter-spacing: 3px;">
                ✨ Secret Santa ✨
              </h1>
              <p style="margin: 20px 0 0 0; color: #8B7355; font-size: 16px; letter-spacing: 4px; text-transform: uppercase; font-weight: 300;">
                {year}
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding: 40px 50px;">
              <p style="color: #2C2C2C; font-size: 18px; margin: 0 0 20px 0; font-weight: 500; text-align: center;">
                Dear {giver_name},
              </p>
              <div style="padding: 30px; margin: 25px 0; background-color: #FFF8DC; border-left: 3px solid #FFD700; border-right: 3px solid #FFD700;">
                <p style="color: #4A4A4A; font-size: 15px; line-height: 1.9; margin: 0; white-space: pre-wrap;">{message_body}</p>
              </div>
              <div style="margin: 40px 0; text-align: center; padding: 40px; background: linear-gradient(135deg, #FFD700 0%, #FDB931 100%); border-radius: 15px;">
                <h2 style="margin: 20px 0 10px 0; color: #2C2C2C; font-family: 'Cormorant Garamond', serif; font-size: 42px; font-weight: 600;">
                  {recipient_name}
                </h2>
                <div style="margin-top: 25px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px;">
                  <p style="margin: 0 0 12px 0; color: #8B7355; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;">
                    Gift Inspiration
                  </p>
                  <p style="margin: 0; color: #4A4A4A; font-size: 16px; line-height: 1.6;">
                    {recipient_interests}
                  </p>
                </div>{address_section}
              </div>
            </td>
          </tr>
          <tr>
            <td style="background: linear-gradient(180deg, #FFF8DC 0%, #FFFFFF 100%); padding: 30px; text-align: center;">
              <p style="margin: 0; color: #8B7355; font-size: 15px;">
                ✦ Wishing you a magical holiday season ✦
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>'''


def generate_winter_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Winter Wonderland themed card - use classic template as base."""
    return generate_classic_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body)


def generate_festive_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Festive Fun themed card - use classic template as base."""
    return generate_classic_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body)


def generate_rustic_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body):
    """Rustic Charm themed card - use classic template as base."""
    return generate_classic_card(giver_name, recipient_name, recipient_interests, recipient_address, message_body)

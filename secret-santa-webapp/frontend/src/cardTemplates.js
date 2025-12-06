// Christmas-themed email card templates

export const cardStyles = {
  classic: {
    name: 'Classic Christmas',
    description: 'Traditional red and green with elegant fonts',
    preview: '🎄',
  },
  elegant: {
    name: 'Elegant Gold',
    description: 'Sophisticated gold and white design',
    preview: '✨',
  },
  winter: {
    name: 'Winter Wonderland',
    description: 'Cool blues and snowflakes',
    preview: '❄️',
  },
  festive: {
    name: 'Festive Fun',
    description: 'Bright and playful holiday cheer',
    preview: '🎁',
  },
  rustic: {
    name: 'Rustic Charm',
    description: 'Warm wood tones and cozy vibes',
    preview: '🕯️',
  }
}

export function generateEmailCard(style, giverName, recipientName, recipientInterests, recipientAddress, messageBody) {
  // Generate address section if address is provided
  const addressSection = recipientAddress ? `
                <div style="margin-top: 15px; padding: 15px; background-color: rgba(255,255,255,0.9); border-radius: 10px;">
                  <p style="margin: 0; color: #165B33; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    Their Address
                  </p>
                  <p style="margin: 10px 0 0 0; color: #333333; font-size: 16px;">
                    ${recipientAddress}
                  </p>
                </div>` : '';

  const addressSectionElegant = recipientAddress ? `
                <div style="margin-top: 20px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);">
                  <p style="margin: 0 0 12px 0; color: #8B7355; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; font-weight: 500;">
                    Their Address
                  </p>
                  <p style="margin: 0; color: #4A4A4A; font-size: 16px; line-height: 1.6;">
                    ${recipientAddress}
                  </p>
                </div>` : '';

  const addressSectionWinter = recipientAddress ? `
                <div style="margin-top: 20px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px; border: 2px dashed #3498DB;">
                  <div style="font-size: 24px; margin-bottom: 10px;">📍</div>
                  <p style="margin: 0 0 10px 0; color: #2980B9; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    Where To Send
                  </p>
                  <p style="margin: 0; color: #34495E; font-size: 16px; line-height: 1.6;">
                    ${recipientAddress}
                  </p>
                </div>` : '';

  const addressSectionFestive = recipientAddress ? `
                  <div style="margin-top: 25px; padding: 25px; background-color: #FFFFFF; border-radius: 20px; border: 3px solid #FF8E53; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
                    <div style="font-size: 35px; margin-bottom: 10px;">📬</div>
                    <p style="margin: 0 0 12px 0; color: #4ECDC4; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
                      Send It Here!
                    </p>
                    <p style="margin: 0; color: #2C3E50; font-size: 17px; line-height: 1.6; font-weight: 500;">
                      ${recipientAddress}
                    </p>
                  </div>` : '';

  const addressSectionRustic = recipientAddress ? `
                <div style="margin-top: 25px; padding: 25px; background-color: rgba(255, 249, 240, 0.95); border-radius: 10px; border: 2px solid #8B6F47; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                  <div style="font-size: 30px; margin-bottom: 12px;">🏠</div>
                  <p style="margin: 0 0 12px 0; color: #654321; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">
                    Mailing Address
                  </p>
                  <p style="margin: 0; color: #4A3C28; font-size: 16px; line-height: 1.7;">
                    ${recipientAddress}
                  </p>
                </div>` : '';

  const templates = {
    classic: `
<!DOCTYPE html>
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
          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(90deg, #C41E3A 0%, #8B1538 100%); padding: 40px; text-align: center; border-bottom: 4px solid #FFD700;">
              <h1 style="margin: 0; color: #FFFFFF; font-family: 'Playfair Display', serif; font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                🎅 Secret Santa 🎄
              </h1>
              <p style="margin: 10px 0 0 0; color: #FFD700; font-size: 18px; letter-spacing: 2px;">
                ✦ ${new Date().getFullYear()} ✦
              </p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 50px 40px; background-color: #FDFBF7;">
              <h2 style="color: #C41E3A; font-family: 'Playfair Display', serif; font-size: 32px; margin: 0 0 20px 0; text-align: center;">
                Hello, ${giverName}! 🎁
              </h2>

              <div style="background-color: #FFFFFF; padding: 30px; border-radius: 15px; border-left: 5px solid #165B33; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <p style="color: #333333; font-size: 16px; line-height: 1.8; margin: 0; white-space: pre-wrap;">${messageBody}</p>
              </div>

              <!-- Recipient Box -->
              <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); padding: 30px; border-radius: 15px; margin: 30px 0; text-align: center; box-shadow: 0 6px 20px rgba(255, 215, 0, 0.4);">
                <p style="margin: 0 0 15px 0; color: #8B1538; font-size: 18px; font-weight: 600;">
                  🎯 Your Secret Santa Recipient
                </p>
                <h3 style="margin: 0; color: #C41E3A; font-family: 'Playfair Display', serif; font-size: 36px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
                  ${recipientName}
                </h3>
                <div style="margin-top: 20px; padding: 20px; background-color: rgba(255,255,255,0.9); border-radius: 10px;">
                  <p style="margin: 0; color: #165B33; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    Their Interests
                  </p>
                  <p style="margin: 10px 0 0 0; color: #333333; font-size: 16px; font-style: italic;">
                    ${recipientInterests}
                  </p>
                </div>${addressSection}
              </div>
            </td>
          </tr>

          <!-- Footer -->
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
</html>`,

    elegant: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=Montserrat:wght@300;500&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #f8f8f8; font-family: 'Montserrat', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f8f8f8; padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFFFFF; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.15);">
          <!-- Decorative Border -->
          <tr>
            <td style="background: linear-gradient(90deg, #FFD700 0%, #FFF8DC 50%, #FFD700 100%); height: 8px;"></td>
          </tr>

          <!-- Header -->
          <tr>
            <td style="padding: 50px 40px 30px 40px; text-align: center; background: linear-gradient(180deg, #FFFFFF 0%, #FFF8DC 100%);">
              <h1 style="margin: 0; color: #2C2C2C; font-family: 'Cormorant Garamond', serif; font-size: 52px; font-weight: 300; letter-spacing: 3px;">
                ✨ Secret Santa ✨
              </h1>
              <div style="width: 100px; height: 2px; background: linear-gradient(90deg, transparent 0%, #FFD700 50%, transparent 100%); margin: 20px auto;"></div>
              <p style="margin: 0; color: #8B7355; font-size: 16px; letter-spacing: 4px; text-transform: uppercase; font-weight: 300;">
                ${new Date().getFullYear()}
              </p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 40px 50px;">
              <p style="color: #2C2C2C; font-size: 18px; margin: 0 0 10px 0; font-weight: 500; text-align: center;">
                Dear ${giverName},
              </p>

              <div style="padding: 30px; margin: 25px 0; background-color: #FFF8DC; border-left: 3px solid #FFD700; border-right: 3px solid #FFD700;">
                <p style="color: #4A4A4A; font-size: 15px; line-height: 1.9; margin: 0; white-space: pre-wrap;">${messageBody}</p>
              </div>

              <!-- Recipient Box -->
              <div style="margin: 40px 0; text-align: center; padding: 40px; background: linear-gradient(135deg, #FFD700 0%, #FDB931 100%); border-radius: 15px; position: relative; box-shadow: 0 10px 30px rgba(253, 185, 49, 0.3);">
                <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background-color: #FFFFFF; padding: 5px 20px; border-radius: 20px; border: 2px solid #FFD700;">
                  <p style="margin: 0; color: #8B7355; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; font-weight: 500;">
                    Your Assignment
                  </p>
                </div>

                <h2 style="margin: 20px 0 10px 0; color: #2C2C2C; font-family: 'Cormorant Garamond', serif; font-size: 42px; font-weight: 600;">
                  ${recipientName}
                </h2>

                <div style="margin-top: 25px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);">
                  <p style="margin: 0 0 12px 0; color: #8B7355; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; font-weight: 500;">
                    Gift Inspiration
                  </p>
                  <p style="margin: 0; color: #4A4A4A; font-size: 16px; line-height: 1.6; font-style: italic;">
                    ${recipientInterests}
                  </p>
                </div>${addressSectionElegant}
              </div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background: linear-gradient(180deg, #FFF8DC 0%, #FFFFFF 100%); padding: 30px; text-align: center;">
              <p style="margin: 0; color: #8B7355; font-size: 15px; font-weight: 300; letter-spacing: 1px;">
                ✦ Wishing you a magical holiday season ✦
              </p>
            </td>
          </tr>

          <!-- Decorative Border -->
          <tr>
            <td style="background: linear-gradient(90deg, #FFD700 0%, #FFF8DC 50%, #FFD700 100%); height: 8px;"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`,

    winter: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Raleway:wght@300;700&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #E8F4F8; font-family: 'Quicksand', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(180deg, #E8F4F8 0%, #D0E8F2 100%); padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFFFFF; border-radius: 25px; overflow: hidden; box-shadow: 0 15px 50px rgba(52, 152, 219, 0.2); border: 3px solid #B8E6F5;">
          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%); padding: 50px 40px; text-align: center; position: relative;">
              <div style="font-size: 60px; margin-bottom: 10px; line-height: 1;">❄️</div>
              <h1 style="margin: 0; color: #FFFFFF; font-family: 'Raleway', sans-serif; font-size: 48px; font-weight: 700; text-shadow: 2px 2px 8px rgba(0,0,0,0.2);">
                Secret Santa
              </h1>
              <p style="margin: 15px 0 0 0; color: #B8E6F5; font-size: 16px; letter-spacing: 3px; text-transform: uppercase; font-weight: 300;">
                Winter Edition ${new Date().getFullYear()}
              </p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 50px 45px; background: linear-gradient(180deg, #FFFFFF 0%, #F0F8FF 100%);">
              <h2 style="color: #2980B9; font-family: 'Raleway', sans-serif; font-size: 28px; font-weight: 700; margin: 0 0 20px 0; text-align: center;">
                ❄️ Hello, ${giverName}! ❄️
              </h2>

              <div style="background-color: #FFFFFF; padding: 30px; border-radius: 15px; border: 2px solid #B8E6F5; margin: 25px 0; box-shadow: 0 4px 15px rgba(52, 152, 219, 0.1);">
                <p style="color: #34495E; font-size: 16px; line-height: 1.8; margin: 0; white-space: pre-wrap;">${messageBody}</p>
              </div>

              <!-- Recipient Box -->
              <div style="background: linear-gradient(135deg, #B8E6F5 0%, #85D8F5 100%); padding: 40px; border-radius: 20px; margin: 35px 0; text-align: center; box-shadow: 0 8px 25px rgba(52, 152, 219, 0.3); border: 3px solid #3498DB;">
                <div style="font-size: 40px; margin-bottom: 15px;">🎁</div>
                <p style="margin: 0 0 10px 0; color: #2C3E50; font-size: 16px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">
                  Your Winter Wonderland Match
                </p>
                <h3 style="margin: 10px 0; color: #2980B9; font-family: 'Raleway', sans-serif; font-size: 40px; font-weight: 700; text-shadow: 1px 1px 3px rgba(255,255,255,0.8);">
                  ${recipientName}
                </h3>

                <div style="margin-top: 25px; padding: 25px; background-color: rgba(255,255,255,0.95); border-radius: 12px; border: 2px dashed #3498DB;">
                  <div style="font-size: 24px; margin-bottom: 10px;">⭐</div>
                  <p style="margin: 0 0 10px 0; color: #2980B9; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    What They Love
                  </p>
                  <p style="margin: 0; color: #34495E; font-size: 16px; line-height: 1.6;">
                    ${recipientInterests}
                  </p>
                </div>${addressSectionWinter}
              </div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%); padding: 35px; text-align: center;">
              <div style="font-size: 30px; margin-bottom: 10px;">❄️ ⛄ ❄️</div>
              <p style="margin: 0; color: #FFFFFF; font-size: 16px; font-weight: 600;">
                Stay Warm & Keep The Secret!
              </p>
              <p style="margin: 10px 0 0 0; color: #B8E6F5; font-size: 13px;">
                Let it snow, let it snow, let it snow! ❄️
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`,

    festive: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Poppins:wght@400;700&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%); font-family: 'Poppins', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFFFFF; border-radius: 30px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.3); border: 6px solid #FFE66D;">
          <!-- Header with pattern -->
          <tr>
            <td style="background: repeating-linear-gradient(45deg, #C41E3A, #C41E3A 20px, #165B33 20px, #165B33 40px); padding: 8px;"></td>
          </tr>

          <tr>
            <td style="background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); padding: 45px 40px; text-align: center;">
              <div style="font-size: 70px; line-height: 1; margin-bottom: 10px;">🎉🎁🎊</div>
              <h1 style="margin: 0; color: #FFFFFF; font-family: 'Fredoka', sans-serif; font-size: 52px; font-weight: 600; text-shadow: 3px 3px 0px rgba(0,0,0,0.2);">
                SECRET SANTA!
              </h1>
              <div style="display: inline-block; background-color: #FFE66D; padding: 8px 25px; border-radius: 20px; margin-top: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                <p style="margin: 0; color: #2C3E50; font-size: 18px; font-weight: 700; letter-spacing: 2px;">
                  ${new Date().getFullYear()}
                </p>
              </div>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 45px 40px; background: linear-gradient(180deg, #FFF9E6 0%, #FFFFFF 100%);">
              <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: inline-block; background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%); padding: 15px 35px; border-radius: 25px; box-shadow: 0 6px 20px rgba(78, 205, 196, 0.4);">
                  <h2 style="margin: 0; color: #FFFFFF; font-family: 'Fredoka', sans-serif; font-size: 32px; font-weight: 600;">
                    Hey ${giverName}! 🎈
                  </h2>
                </div>
              </div>

              <div style="background: linear-gradient(135deg, #FFFFFF 0%, #FFF9E6 100%); padding: 30px; border-radius: 20px; border: 3px dashed #FF8E53; margin: 25px 0; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
                <p style="color: #2C3E50; font-size: 16px; line-height: 1.8; margin: 0; white-space: pre-wrap;">${messageBody}</p>
              </div>

              <!-- Recipient Box -->
              <div style="margin: 40px 0;">
                <div style="text-align: center; margin-bottom: 20px;">
                  <div style="font-size: 50px; line-height: 1;">🎯✨</div>
                </div>

                <div style="background: linear-gradient(135deg, #FFE66D 0%, #FFBE53 100%); padding: 40px; border-radius: 25px; text-align: center; box-shadow: 0 10px 30px rgba(255, 190, 83, 0.4); border: 4px solid #FF8E53; position: relative;">
                  <div style="position: absolute; top: -20px; left: 20px; font-size: 40px; transform: rotate(-20deg);">🎄</div>
                  <div style="position: absolute; top: -20px; right: 20px; font-size: 40px; transform: rotate(20deg);">🎅</div>

                  <p style="margin: 0 0 15px 0; color: #C41E3A; font-size: 20px; font-weight: 700; text-transform: uppercase; letter-spacing: 3px;">
                    🌟 You're Buying For 🌟
                  </p>
                  <h3 style="margin: 0; color: #2C3E50; font-family: 'Fredoka', sans-serif; font-size: 46px; font-weight: 600; text-shadow: 2px 2px 0px rgba(255,255,255,0.5);">
                    ${recipientName}
                  </h3>

                  <div style="margin-top: 30px; padding: 25px; background-color: #FFFFFF; border-radius: 20px; border: 3px solid #FF8E53; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
                    <div style="font-size: 35px; margin-bottom: 10px;">💝</div>
                    <p style="margin: 0 0 12px 0; color: #4ECDC4; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
                      Gift Ideas
                    </p>
                    <p style="margin: 0; color: #2C3E50; font-size: 17px; line-height: 1.6; font-weight: 500;">
                      ${recipientInterests}
                    </p>
                  </div>${addressSectionFestive}
                </div>
              </div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%); padding: 35px; text-align: center;">
              <div style="font-size: 40px; margin-bottom: 15px; line-height: 1;">🎊 🎁 🎉 🎄 ⭐</div>
              <p style="margin: 0; color: #FFFFFF; font-size: 18px; font-weight: 700; font-family: 'Fredoka', sans-serif;">
                HAVE A BLAST! 🚀
              </p>
              <p style="margin: 10px 0 0 0; color: #FFF9E6; font-size: 14px; font-weight: 400;">
                Remember: Shhh... it's a secret! 🤫
              </p>
            </td>
          </tr>

          <tr>
            <td style="background: repeating-linear-gradient(45deg, #C41E3A, #C41E3A 20px, #165B33 20px, #165B33 40px); padding: 8px;"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`,

    rustic: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;700&family=Cabin:wght@400;600&display=swap');
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #F5F1E8; font-family: 'Cabin', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(180deg, #F5F1E8 0%, #E8DCC8 100%); padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFF9F0; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 40px rgba(101, 67, 33, 0.3); border: 8px solid #8B6F47;">
          <!-- Wood grain header -->
          <tr>
            <td style="background: linear-gradient(90deg, #654321 0%, #8B6F47 50%, #654321 100%); padding: 5px;"></td>
          </tr>

          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(180deg, #A0826D 0%, #8B6F47 100%); padding: 50px 40px; text-align: center; position: relative;">
              <div style="font-size: 60px; margin-bottom: 15px; line-height: 1;">🕯️</div>
              <h1 style="margin: 0; color: #FFF9F0; font-family: 'Merriweather', serif; font-size: 48px; font-weight: 700; text-shadow: 3px 3px 6px rgba(0,0,0,0.4);">
                Secret Santa
              </h1>
              <div style="width: 80px; height: 3px; background-color: #D4A574; margin: 20px auto;"></div>
              <p style="margin: 0; color: #F5DEB3; font-size: 16px; letter-spacing: 3px; text-transform: uppercase; font-weight: 400;">
                Cozy Holidays ${new Date().getFullYear()}
              </p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 50px 45px; background-color: #FFF9F0;">
              <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: inline-block; background-color: #C41E3A; padding: 12px 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(196, 30, 58, 0.3);">
                  <h2 style="margin: 0; color: #FFF9F0; font-family: 'Merriweather', serif; font-size: 28px; font-weight: 700;">
                    Dear ${giverName} 🎄
                  </h2>
                </div>
              </div>

              <div style="background-color: #FEFCF7; padding: 30px; border-radius: 10px; border: 2px solid #D4A574; margin: 25px 0; box-shadow: inset 0 2px 8px rgba(0,0,0,0.05);">
                <p style="color: #4A3C28; font-size: 16px; line-height: 1.9; margin: 0; white-space: pre-wrap;">${messageBody}</p>
              </div>

              <!-- Recipient Box -->
              <div style="background: linear-gradient(135deg, #D4A574 0%, #C19A6B 100%); padding: 40px; border-radius: 12px; margin: 35px 0; text-align: center; box-shadow: 0 8px 25px rgba(180, 140, 100, 0.4); border: 4px solid #8B6F47; position: relative;">
                <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%);">
                  <div style="background-color: #654321; padding: 8px 25px; border-radius: 20px; border: 3px solid #D4A574;">
                    <p style="margin: 0; color: #FFF9F0; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; font-weight: 600;">
                      🎁 Your Match 🎁
                    </p>
                  </div>
                </div>

                <div style="margin-top: 15px; font-size: 45px; line-height: 1;">🎅</div>

                <h3 style="margin: 15px 0; color: #4A3C28; font-family: 'Merriweather', serif; font-size: 42px; font-weight: 700; text-shadow: 2px 2px 4px rgba(255, 249, 240, 0.5);">
                  ${recipientName}
                </h3>

                <div style="margin-top: 30px; padding: 25px; background-color: rgba(255, 249, 240, 0.95); border-radius: 10px; border: 2px solid #8B6F47; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                  <div style="font-size: 30px; margin-bottom: 12px;">🌲</div>
                  <p style="margin: 0 0 12px 0; color: #654321; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">
                    Gift Inspiration
                  </p>
                  <p style="margin: 0; color: #4A3C28; font-size: 16px; line-height: 1.7; font-style: italic;">
                    ${recipientInterests}
                  </p>
                </div>${addressSectionRustic}
              </div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background: linear-gradient(180deg, #8B6F47 0%, #654321 100%); padding: 35px; text-align: center;">
              <div style="font-size: 35px; margin-bottom: 12px; line-height: 1;">🕯️ ✨ 🕯️</div>
              <p style="margin: 0; color: #F5DEB3; font-size: 17px; font-weight: 600; font-family: 'Merriweather', serif;">
                Warm Wishes & Cozy Vibes
              </p>
              <p style="margin: 12px 0 0 0; color: #D4A574; font-size: 14px; font-weight: 400;">
                May your holidays be merry and bright! 🌟
              </p>
            </td>
          </tr>

          <tr>
            <td style="background: linear-gradient(90deg, #654321 0%, #8B6F47 50%, #654321 100%); padding: 5px;"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`
  }

  return templates[style] || templates.classic
}

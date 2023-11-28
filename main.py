from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN: Final = '(masukan kode token kamu)'
BOT_USERNAME: Final = '@(masukan nama botmu)'
#ini adalah pilihan commandnya
async def start_command(update: Update, context: Application):
    await update.message.reply_text("Hello! Thanks Sudah ngobrol sama gue!")

async def help_command(update: Update, context: Application):
    await update.message.reply_text("Gue hanya AI, pasti lo gabut sama gue kan")

async def custom_command(update: Update, context: Application):
    await update.message.reply_text("ini command custom")        
#ini adalah respon dari bot
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'apaan coy'
    
    if 'apa kabar' in processed:
        return 'kabare baek jon'
    
    if 'gue suka sama lo' in processed:
        return 'gue cuma AI'
        
    return 'kaga paham gue bahasa lo, ngomong yang bener dikit napa'

async def handle_message(update: Update, context: Application):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('bot', response)
    await update.message.reply_text(response)

async def error(update: Update, context: Application):
    print(f'update{update} caused error {context.error}')

if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(error)

    # pollings
    print('Polling...')
    app.run_polling()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

BOT_TOKEN = "7732391797:AAHsSB-vJsLmGq0glX7jB-jh_fe9FXbmLbE"
REFERRAL_CODE =48198037 "https://freebitco.in/?r=48198037"

# Store user referrals
user_data = {}

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {"referrals": 0, "invited": []}
    
    message = """
Welcome to the BTC Spinner bot!
Claim 0.001 BTC by inviting friends to join!
Each user you invite unlocks your claim rewards.

Type /claim to check your earnings.
"""
    update.message.reply_text(message)

def claim(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in user_data:
        update.message.reply_text("Please use /start to get started.")
        return

    referrals_needed = 5
    if user_data[user_id]["referrals"] < referrals_needed:
        update.message.reply_text(f"You need {referrals_needed - user_data[user_id]['referrals']} more referrals to unlock your claim.")
        return

    earnings = f"You earned {random.choice([0.0001, 0.0002, 0.0003, 0.0005, 0.001])} BTC!"
    update.message.reply_text(earnings)
    update.message.reply_text(f"Now, join FreeBitcoin using this link to earn more: https://freebitco.in/?r={48198037}")

def referral(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if len(context.args) == 0:
        update.message.reply_text("Please provide a referral code after the command.")
        return

    ref_code = context.args[0]
    if ref_code == REFERRAL_CODE:
        if user_id not in user_data:
            user_data[user_id] = {"referrals": 1, "invited": [user_id]}
        else:
            user_data[user_id]["referrals"] += 1
            user_data[user_id]["invited"].append(user_id)
        update.message.reply_text(f"Thank you for inviting! You now have {user_data[user_id]['referrals']} referrals.")
    else:
        update.message.reply_text("Invalid referral code.")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("claim", claim))
    dp.add_handler(CommandHandler("referral", referral))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
  

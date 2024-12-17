### Code Description

This Python script automates sending an email using the `smtplib` library and schedules the task with `schedule`. It sends an email every 24 hours.

#### Functionality:
1. **Send Email**: 
   The script creates an email with a subject, sender, recipient, and message content, then sends it via Gmail's SMTP server (`smtp.gmail.com`) using SSL on port 465.

2. **Scheduling**:
   The `schedule` library is used to run the email-sending function every 24 hours with `schedule.every(24).hours.do(Emailsending)`.

3. **Continuous Execution**:
   The script runs in an infinite loop (`while True`) and checks for pending tasks every second using `schedule.run_pending()`.

#### Requirements:
- **Libraries**: 
  - `schedule` for scheduling tasks.
  - `smtplib` for sending emails via Gmail's SMTP server.
  - `email.message` to create and configure the email.

#### How to Use?
Change 'your_gmail.com' on line 7 to your Gmail address and 'your_password' as well.

On line 13, change 'title' to the title of the email that the program will send.

On line 15, change 'other_person@gmail.com' to the email address of the recipient.

On line 16, change 'message that you want' to the message you want to send.

Remember to keep the quotes, just change the text inside.

Run the code.

You can change the time in line 31 if you want to adjust the interval.

#### Security Considerations:
- It's recommended to store sensitive credentials securely (e.g., using environment variables) instead of hardcoding them in the script.

### Use Case:
This script can be used to automate sending reports, notifications, or reminders via email at regular intervals.

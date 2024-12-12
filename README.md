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

#### Security Considerations:
- It's recommended to store sensitive credentials securely (e.g., using environment variables) instead of hardcoding them in the script.

### Use Case:
This script can be used to automate sending reports, notifications, or reminders via email at regular intervals.

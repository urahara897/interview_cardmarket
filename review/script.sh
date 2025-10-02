STDOUT="/dev/stdout"
LOG_FILE='$STDOUT'
LOG_MESSAGE='is the date, should log to $STDOUT'

# log with timestamp
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOGFILE"
}

log_message $LOG_MESSAGE


** I was asked to review the shell script in `shell/script.sh`. Here's my feedback: 

Variable Quoting Issues

LOG_FILE='$STDOUT' , Here the single quotes prevent variable expansion
LOG_MESSAGE='is the date, should log to $STDOUT'  # The Same issue is occuring as before

Single quotes prevent variable expansion.
In this scenario, it means $STDOUT would not be replaced with /dev/stdout.
The end result would be the script not working as intended.

We should instead use double quotes to allow variable expansion.




LOG_FILE="$STDOUT"
LOG_MESSAGE="is the date, should log to $STDOUT"

log_message $LOG_MESSAGE : In my opinion it would be better if we use double quotes here.

Reason: In my opinion if LOG_MESSAGE contains any space, it could break the script.
So for me, the best practice is to use double quotes here for the script to be more robust.

For example:
log_message "$LOG_MESSAGE"



If this script is going to be used in production, I would add some error handing

For example: 
log_message() {
    if ! echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE" 2>/dev/null; then
        echo "Failed to write to log file" >&2
        return 1
    fi
}

**


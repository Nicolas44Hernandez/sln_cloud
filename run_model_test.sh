#!/bin/bash

declare -a LOG_FILES=("app.log"
                      "api-rest.log"
                      "mongo.log"
                      rtd.log
                      )

export TEST_NAME="HOME_MLP_16_16_16_3ST_SC3_OFF"
export TEST_DURATION_IN_MINUTES=12
export APP_MODE="RUN"

# Create log files
rm -r logs
mkdir logs
for log_file in "${LOG_FILES[@]}"
do
    if ! test -f "logs/$log_file"; then
        touch "logs/$log_file"
    fi
done

echo ------------------------------
echo Running model test

# Run flask app 
export FLASK_APP="backend/server/app:create_app()"
export FLASK_ENV="DEVELOPMENT"
flask run --host '0.0.0.0' --port 3000 &


# Set end
echo ------------------------------
TEST_END_TIME=`expr $TEST_DURATION_IN_MINUTES + 1`
echo Test stop at: 
echo "pkill -f 'flask run'" | at now +$TEST_END_TIME minutes

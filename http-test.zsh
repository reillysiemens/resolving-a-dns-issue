#!/usr/bin/env zsh

# 720 * 10s = 2hrs
: ${INTERVAL=10}
: ${NUM_TESTS=720}

: ${ROUTER_IP="192.168.1.1"}
: ${ROUTER_HOSTNAME="router.asus.com"}

: ${OUTPUT_FILE="./http-test-results.csv"}

function now() {
    # ISO 8601 FTW!
    date -u "+%Y-%m-%dT%H:%M:%SZ"
}

function http-test() {
    local host=$1
    /usr/bin/time -f "%e" curl -s $host > /dev/null
}

function run-tests() {
    # Create CSV header.
    echo "Datetime,Seconds for HTTP GET by IP,Seconds for HTTP GET by Hostname"

    # A sample CSV row will look like
    # 2018-03-26T03:37:29Z,0.01,0.02

    # For each iteration spit out the current time, how long it takes to curl
    # with an IP address, and how long it takes to curl with a hostname.
    for t in {1..${NUM_TESTS}}
    do
        # Redirect stderr to stdout with 2>&1 to capture GNU time's output.
        echo "$(now),$(http-test ${ROUTER_IP} 2>&1),$(http-test ${ROUTER_HOSTNAME} 2>&1)"
        sleep ${INTERVAL}
    done
}

run-tests >> ${OUTPUT_FILE}

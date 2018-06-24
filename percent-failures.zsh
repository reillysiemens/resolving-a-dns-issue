#!/usr/bin/env zsh
function percent_failures() {
    local file="${1}"
    local pattern="${2}"
    local num_failures=$(grep $pattern $file | wc -l)
    local num_results=$(wc -l $file | cut -d\  -f1)
    echo "scale=4; ${num_failures} / ${num_results} * 100" | bc -l
}

percent_failures before.csv '5\.'
percent_failures after.csv '5\.'

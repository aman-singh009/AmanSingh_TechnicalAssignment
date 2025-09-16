#!/bin/bash
# Run all 6 producers in background

python erp_producer.py &
python iot_producer.py &
python clinical_producer.py &
python social_producer.py &
python regulatory_producer.py &
python finance_producer.py &

echo "All producers started!"

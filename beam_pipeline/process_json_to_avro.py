import apache_beam as beam
import json
import time
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime

def parse_json(line):
    record = json.loads(line)
    timestamp_str = record["Timestamp"]
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    record["Timestamp_unix"] = int(time.mktime(dt.timetuple()) * 1000)
    return record

def run(input_path, output_path, schema_path):
    options = PipelineOptions()
    with open(schema_path, "r") as f:
        schema = f.read()

    with beam.Pipeline(options=options) as p:
        (p
         | "Read JSON Lines" >> beam.io.ReadFromText(input_path)
         | "Parse JSON and Add Timestamp_unix" >> beam.Map(parse_json)
         | "Write to Avro" >> beam.io.WriteToAvro(
                output_path,
                schema=schema,
                file_name_suffix=".avro"
            ))

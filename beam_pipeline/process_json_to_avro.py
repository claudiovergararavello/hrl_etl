import apache_beam as beam
import json
import time
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime
import os
import sys

'''
print(">>> Iniciando conversión JSONL → AVRO")
print(">>> Argumentos recibidos:")
print("    input_path:", sys.argv[1])
print("    output_dir:", sys.argv[2])

# Verificar existencia de archivos
print(">>> Verificando existencia de archivos:")
print("    ¿Existe el input?", os.path.exists(sys.argv[1]))
print("    ¿Existe el output_dir?", os.path.exists(sys.argv[2]))

# Verifica que se pueda escribir en output_dir
try:
    test_path = os.path.join(sys.argv[2], "test_write.txt")
    with open(test_path, "w") as f:
        f.write("test")
    os.remove(test_path)
    print(">>> OK: Se puede escribir en el directorio de salida.")
except Exception as e:
    print(">>> ERROR al escribir en el directorio de salida:", e)
'''

def parse_json(line):
    record = json.loads(line)
    timestamp_str = record["Timestamp"]
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    record["Timestamp_unix"] = int(time.mktime(dt.timetuple()) * 1000)
    return record

def run(input_path, output_path, schema_path):
    options = PipelineOptions()
    with open(schema_path, "r") as f:
        schema = json.load(f)

    with beam.Pipeline(options=options) as p:
        (p
         | "Leer Data de JSONL" >> beam.io.ReadFromText(input_path)
         | "Parseo del JSON y Agregación de campo Timestamp_unix" >> beam.Map(parse_json)
         | "Escritura en AVRO" >> beam.io.WriteToAvro(
                output_path,
                schema=schema,
                file_name_suffix=".avro",
                use_fastavro=False
            ))

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    schema_path = sys.argv[3]
    run(input_path, output_path, schema_path)

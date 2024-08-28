from datetime import datetime
from tableauhyperapi import Connection, HyperProcess, SqlType, TableDefinition, Inserter, CreateMode, TableName, Telemetry, escape_name, escape_string_literal

hyper = HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU)
hyper_conn = Connection(hyper.endpoint, 'BACDEMO.hyper', CreateMode.NONE)

query_result = hyper_conn.execute_query(query=F'''
    SELECT "row_id", "row_name"
    FROM "Extract"."BACDEMO"
    LIMIT 10
    '''
)

for row in query_result:
    print(row)

hyper_conn.close()
hyper.close()

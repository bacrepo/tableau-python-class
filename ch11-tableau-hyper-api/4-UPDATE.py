from datetime import datetime
from tableauhyperapi import Connection, HyperProcess, SqlType, TableDefinition, Inserter, CreateMode, TableName, Telemetry, escape_name, escape_string_literal
current_date = datetime.now()

hyper = HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU)
hyper_conn = Connection(hyper.endpoint, 'BACDEMO.hyper', CreateMode.NONE)

result = hyper_conn.execute_command(command=F'''
    UPDATE "Extract"."BACDEMO"
    SET "row_name" = 'Test Update ' || CAST("row_id" as VARCHAR(20))
    '''
)

print("Content Hyper File BACDEMO.hyper Updated !")

hyper_conn.close()
hyper.close()


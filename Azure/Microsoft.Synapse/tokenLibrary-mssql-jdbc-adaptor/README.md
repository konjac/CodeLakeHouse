# Token Library adaptor for MSSQL JDBC

This library is used for Synapse Spark to connect Azure SQL in JDBC authenticated with Microsoft Entra ID.

1. Build the project
2. Upload `target/token-library-mssql-jdbc-adaptor-*.jar` and `target/dependency/mssql-jdbc-*.jar` as Spark pool packages.
3. Specify the callback class as `org.konjac.TokenLibraryCallback` in JDBC parameters.
```scala
val df = spark.read
  .format("jdbc")
  .option("url", "jdbc:sqlserver://{serverName}.database.windows.net;database={databaseName}")
  .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")
  .option("query", "select * from sys.tables")
  .option("accessTokenCallbackClass", "org.konjac.TokenLibraryCallback")
  .load()
```
# mssql/__init__.py
# Copyright (C) 2005-2016 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy.dialects.mssql import base, pyodbc

base.dialect = pyodbc.dialect

from sqlalchemy.dialects.mssql.base import (
    INTEGER,
    BIGINT,
    SMALLINT,
    TINYINT,
    VARCHAR,
    NVARCHAR,
    CHAR,
    NCHAR,
    TEXT,
    NTEXT,
    DECIMAL,
    NUMERIC,
    FLOAT,
    DATETIME,
    DATETIME2,
    DATETIMEOFFSET,
    DATE,
    TIME,
    SMALLDATETIME,
    BINARY,
    VARBINARY,
    BIT,
    REAL,
    IMAGE,
    TIMESTAMP,
    MONEY,
    SMALLMONEY,
    UNIQUEIDENTIFIER,
    SQL_VARIANT,
    dialect,
)


__all__ = (
    "INTEGER",
    "BIGINT",
    "SMALLINT",
    "TINYINT",
    "VARCHAR",
    "NVARCHAR",
    "CHAR",
    "NCHAR",
    "TEXT",
    "NTEXT",
    "DECIMAL",
    "NUMERIC",
    "FLOAT",
    "DATETIME",
    "DATETIME2",
    "DATETIMEOFFSET",
    "DATE",
    "TIME",
    "SMALLDATETIME",
    "BINARY",
    "VARBINARY",
    "BIT",
    "REAL",
    "IMAGE",
    "TIMESTAMP",
    "MONEY",
    "SMALLMONEY",
    "UNIQUEIDENTIFIER",
    "SQL_VARIANT",
    "dialect",
)

__version__ = "7.0.1"

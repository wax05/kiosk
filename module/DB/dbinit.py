from DB import SQL

Query1 = """
CREATE TABLE `admin_data` (
	`user_id` VARCHAR(13) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',
	`pw_hash` VARCHAR(64) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci'
)
COMMENT='admin Data'
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;
"""

Query2 = """
CREATE TABLE `get_code` (
	`Code` VARCHAR(5) NOT NULL COLLATE 'utf8mb3_bin',
	`Take` VARCHAR(5) NULL DEFAULT NULL COLLATE 'utf8mb3_bin',
	`Take_T` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	`ProductCode` VARCHAR(15) NULL DEFAULT NULL COLLATE 'utf8mb3_bin',
	PRIMARY KEY (`Code`) USING BTREE
)
COLLATE='utf8mb3_bin'
ENGINE=InnoDB
;
"""

Query3 = """
CREATE TABLE `product_code` (
	`ProductCode` VARCHAR(20) NOT NULL COLLATE 'utf8mb3_bin',
	`ProductName` VARCHAR(20) NULL DEFAULT NULL COLLATE 'utf8mb3_bin',
	PRIMARY KEY (`ProductCode`) USING BTREE
)
COLLATE='utf8mb3_bin'
ENGINE=InnoDB
;
"""

DB = SQL()
if DB.INSERT(Query1):
    print("AdminData")
if DB.INSERT(Query2):
    print("GetCode")
if DB.INSERT(Query3):
    print("ProductCode")

print("END")

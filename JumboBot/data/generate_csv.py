from JumboBot.app import SaveToCSVFromSQL

SQL_path = "JumboBot/data/products.db"
save_to = SaveToCSVFromSQL(SQL_path)
save_to.save()
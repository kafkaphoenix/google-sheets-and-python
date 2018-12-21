import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Legislators 2017').sheet1

pp = pprint.PrettyPrinter()
#legislators = sheet.get_all_records()
#legislators = sheet.col_values()
#legislators = sheet.row_values()
legislators = sheet.cell(6,11).value
#sheet.update_cell(6,11,'789-895-7894')
row = ["a","b","c","d","e","f!"]
index = 3
sheet.insert_row(row, index)
sheet.delete_row(3)
pp.pprint(legislators)
print(sheet.row_count)
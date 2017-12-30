__author__ = 'Admin'
import shelve

file = shelve.open("style/settings")
file['bgColor'] = '#FFFFFF'
file['fontColor'] = '#000000'
file['font'] = 'Calibri'
file['size'] = '14.0'
file.sync()
file.close()
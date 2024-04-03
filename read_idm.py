import nfc
import binascii

# ICカードの待機
clf = nfc.ContactlessFrontend("usb")
print("カードをかざしてください:")
try:
  tag = clf.connect(rdwr={"on-connect": lambda tag: False})
finally:
  clf.close()

# ICカードのID情報抽出して表示する
if tag.TYPE == 'Type3Tag':
  id_info = binascii.hexlify(tag.idm).decode()
elif tag.TYPE == 'Type4Tag':
  id_info = binascii.hexlify(tag.identifier).decode()

print("IDm：" + id_info)

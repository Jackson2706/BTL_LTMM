import cv2
import binascii
import numpy as np
from PIL import Image


def encode(image_path):
    # Đọc ảnh từ tệp tin
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256,256))
    # Chuyển đổi ảnh thành mảng bytes
    image_bytes = cv2.imencode('.jpg', image)[1].tobytes()

    # Chuyển đổi mảng bytes thành mã hex
    hex_code = binascii.hexlify(image_bytes)
    k = len(hex_code)//16
    # In mã hex  
    return hex_code[0:16*k]

def decode(hex_code):
    # Chuyển đổi mã hex thành mảng bytes
    byte_array = binascii.unhexlify(hex_code)

    # Chuyển đổi mảng bytes thành hình ảnh
    image = cv2.imdecode(np.frombuffer(byte_array, np.uint8), cv2.IMREAD_COLOR)

    return image

if __name__ == "__main__":
    hex_code_1 = encode("Anh_the.jpg")
    print(hex_code_1)
    # print(hex_code_1.hex())
    hex_code = b'a9ffb7aaba799363d10db1c789da6a9b0a240207ef7ca672591c19f26bbf42f8f347f43ed06678e7f01271f64254e1dd4f62c90ba658e57db02e28a0bfa92b51f2defe0d854756985ac1f8bfe3efd85cda08f0c7e7e092c964478bb8e41cca5f5475d75c271ea3972fae66687e5a8bea58226430798077125822643079807712582264307980771258226430798077125822643079807712364427fab7f94ab6de3d343bbe2693f19205fac0a9bc3fce2291aa5c1923b9e20868ceedb71336440236970a4da3f79dd2a31dd55f05179dc8a4e080e28b70467d15e535b79427c6f2d65ed5ecb394c9cdd49a0e66c8b49eca1c9ea8dc559c63a032b922ab385274fb458b94cdf5067701cb2c01543ad8c231d46a610e1d73fbe679692bc3952554415dd18dd2961dbac90385fe5dbb588ad6e1e023148318a82f00966568446dd28d3fda8d39d6ba8e3af754cc59a18392062a4ec79efc97266c41975044efa726929bc76de16f7298eea83493572c3279bd9d0e5c56fc9fd57ab9cf02459e054ee0b00e3817a7a55c1e51bc14113f9bc492fe5ed50764bfb6e50e141966fdb0c4d2a31dd55f05179d1b0763a1ba09fe5cdb6eec1990f003ced900b77ff9b3faa8f209a8b904bd5c388fe783edd4e082a6a869e80aff73288f84ddc57f370b04093d9e6e054d8b58c2462c10ac5975076be5ff6cb7ff96371c1a297d40a5f4545faf5e8a8029a2c3b7e0599168f2e507988eb5bbeebf815aee8c29965987cbdafd96f2a961f3812dbad1381874f237ffd33f7ff0295299c905b23ac0cbb4956c21b71ad8b809515dd8667f4bc13eaa1178a698503d4fd6149de0b00e3817a7a55c3db577bbb273c130a860911c356806f8e8c092979d0f593bdae94e9b4292d9733e76aecd8d01b6df56da4e7e3c649e1afa734c6c6c2d14c885a4c8587d1ef54b66ef815a62c38b0c9470186a0e47adaff23376687ac584adf82405ef750a693632ebe6ed9094c3e9e2d42180d1f1fd3fd4f97e88d6de31acee4f77d7fd12220784ce6bfb830aca02dbdd20f3049ad9f362a0dc856d984d9c34d594eb5a0228b20239e576d5d06ce9c6bde43195a7ac2981084a91ad25dcd59540acd686aac2b9927d91a2eba73319e7c384a69c0436acea17a2cf426715ecc6fd6ef0ce9c10dffda55f794b85f80adbf357f881bb9637e215aa99ab591af362aaaaeace95f18c56c8c87762b84c2fefb18b0d92ba5e3916afb81fe88b3ca1455625265fdd29ad2e5c37637d0e2268b15e7b3651fe5f8d3122f49a430348f1392fb020703222fbaabd11fafbdf806b56e6bdabec0ffa84019113a0e3bd3e359b587059dc0ab50e4c5bc37b1c6f5b145ae9f73d3429479b3905fc65aae03d4026796fa9c9c8a4fe3c061c3b03d9cc599c9fbb8aee54092405ad1ebd88561d1b7811e222e36b948702bc9283f20457b188eba4a1bf81471bdf704b4197b444c9f2d64a04807b35680660796910a7d7f87199fd13a9a1478fbdf0d47cc372824a5f6fba3b85208d4d8be19d730e0b6cf09194c488a1474480ba5caa4467921b5cd51fa598d9b96cb537993e8d09202dbc17ef4a6e841a63481a474581368ba084f4964bb64f0f39f4ec9b65d49affade43db93fbdcbf454680f712076e31952ffac25ff212bf0d95652825a1b0ee05cac0f7976ad8f2b11766c9f47064ddef6705c2c0c4f7fd876f7d4ae55a1d3ada4ff332edc6c6f4d5068e359bac6ed829d263011605a5fa24bcf2e5edd7d446eed3acfa58f057f212fcada9b3c236b6d2f33caa42c1265344ae225016a3a0a5cd6018c76512f52a5da8ed23ae09b6db901f08af52f539cf54235a12e39f4c08dedd10955fd476538113df37716e5fec64dd3cf61f8491ee5c7cdca2d6584d50f8ef9baf4cda2d10266249e1a8a31bd168c54d70e4c0c11dea83c6c0b9ebcaa880ec262cb581e93624c43c5017941b56570eda01aeebbd28517e9f141de713b6255b048d584fe331f83b8a03e76c490d22104aa3c84ef64c9115a33ccb9b3af20956f5d3f4e68e17eab96e13ef43ea9216d49fcf3898254abf6e4bebb770924c903dbd3919a3e109138b20f4102a81e1b52bdc569a1bbec0b713a62d8fdcac10a46c5d8bda4dfc8dda164452c5e4996ea1120f4f9cba3a8d87ec9355a94076a898e3b6f71765b6e871d7d8e5014bdf7c35f5d9e9388b3a50c526ce4d2954cbbca2a76da49331c487cdfdf921f0f68e16fe9abddbed9b7de419af48ba4c6f5ad5f28aa09dde8612f81376db7f32afeadb7afa72082ca32b8f91202a5892be5a6c44b40c499adcf1ec01d73e8fa059ebf7f119810ef3ea681f2c256bc34748b4f12eea0fe3a6357fbedbab386314ca77932c4be43367509cf4b917dbbac3540a645c2273e066800fed9bfed088a9874bfca9d5cf2809df41234a2faa395fc1328a30d243efe54ba263fd62e0883df9f3bf40b93bf1c422e0ef564b270fe261f75dede9044d6c02d5baab4b4fbeb7907520b449853dfbb3508a14d5a5579cd8b98a93a2594b2242017514d38b75d3eeafeb616daaf79c5fb5844e19a27534d9eae1086aa948c7324263355283a6da9e52a407a5b63f8b37288d4a6bc709fcb0241d08f607b6d14a29008f3ee635aea75c9c5930fc6c19d28160f9a3474bff93a6d5a858633c113b4aec1d3c3836c7467514c5702ef8e0e5c94a48ef98098a85ed91538995b831cf26e15a30fb196955401d0c65df852b52f90b8b9decac670a101ebc27aa42064c6294efb1071689a1d8b7afb2609363de678340c7beda0a8a277b785bf40433c3739e09e867ee71d52cd2e35ada48a72bb479d9e2d60528ade956be816d442689b7135da2c11ace3c330755c5f1fe01937701b3f4b18ec9e3efb3a816b4da1e336a5b6b15477e0e285818a803d85ca7e650a183b32a3afff8ac5dcc8b32a5a9f9861ed1e97eb05816ab451c85e3abb9dbd5e73a4be8f4358a50915b77df6634e1a684c45a0f5f162ad6fe0f1360b47d24378389494eac212a5fb2645d57ef7328efb271ff7643ec848133632995ddc220d73417afc790468cf172d07d6664836008008fd3bb424c19a6f8c32ad56bda479058bc7b3492604f7c369f8a7285d39ebff9d5cb79639523b236464b73bad9ec0a939a77501877c034797e055f31ada3adef5ff2a2638c42d924ac5284b5bc63e47b6c23ed073078975b3a9259b033a6d4a97f31c05ff475601c4005c90f00a224278d3b881b63b3229e1e27ed3a4d3c7925975659c768061196dd48ebf8d6565471a49cf7359f02aa433ec2d9e301cb451f522216b423fc6bca022c4b2acef4fdd621234a25675eab6cf109bad2c4bcd7e2635711094e46c60c499d6b9b96d348c230a9ca231a8d47a4cb61531a4653a259922e77667bc8a94f8c1067f5da5259ca8bc96bbacefa5e5c20e20d5fac71350a05e01ab13e20ab10eae616e8ae2b51fd2492d8d826dc715be5c30b5780cf501d69e60c83bec18258fa253798316836c5cd2f074a6fb520a1c87eb373b540bccd6e8b74bb20bb06c268e38d1b27517117fa16865cf03ca457a4214923b71e2f2af4cf97457aa30709add323d132f6e540937092c467a724e4229eb5058a3d2c7fc12657375f454dd4068ee7c069eeaed7a0428cab2ffeab7363bda7f346a1788229c338428b5ed1c6b1d7c7dbdfd9ff19dc5a394684880626a60c5b0d80bb647dd24289365c179d87fb7144a6c181312107a2ae39e4389069a3d7f6d4b92d4297fcb71629d42f24f53cd9f86ba21e34104da00162f6c226f07fccd2d5a561f455e6622f77e1295e339c155c8dd054cc05827bfa9306a8fc0dc522daf01a12d5e5b4ff8ed6c24fbe1fd9a73a8e121ac4cf04870239c308b7033ba98f72f3d34d954c66993816e64952b09074f03eb4363a51a7c8720ee2a9eb7f758db4f244304b328bc6c97ac38a20a53d23a24ce7fd299561f3dc907f350b5d07192d68ab1e4a204e5f62e319b3d5298155c9aee511cd53077c3d485d75308d3a434cb92debb6682c182838cc291eaccb7cd9f8bd9e0f58f913ac9d4e6190185ed4e38ff4e0174c3f05b760a9b9005f4366761851094b5aff8d86e886b64bdada87b32c66d5ab3ba5bbbfc302882fbcfe669cc24647bc3496036fe40d3a5dea5f7af6799ac3f87fd363f6760a6383a91953520d928c88aa86fbc2c808d07eecbc3'
    image = decode(hex_code)        
    image_1 = decode(hex_code_1)
    # print(image_1)
    # print(type(image))
    # print(type(image_1))
    #cv2.imshow("image", image)
    cv2.imshow("image_1", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
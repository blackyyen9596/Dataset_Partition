import os, shutil, glob, random
# 定義資料集名稱
sets = ['train', 'validation', 'test']
# 定義類別名稱
classes = ['cat', 'dog']
# 訓練集佔整體資料集比例
train_percent = 0.7
# 驗證集佔整體資料集比例  
val_percent = 0.15
# 測試集佔整體資料集比例 
test_percent = 0.15  
# 解壓縮資料夾所在的路徑
original_dataset_dir = r'C:\Users\Blacky\Desktop\deep_learning_in_keras\dataset\dogs-vs-cats\train'
# 用來儲存資料集的位置
base_dir = r'C:\Users\Blacky\Desktop\deep_learning_in_keras\dataset\dogs-vs-cats\cats_and_dogs_small'

val_percent = val_percent/(val_percent + test_percent)
test_percent = 1
dataset_percent = [train_percent, val_percent, test_percent]

# 如果儲存資料集的資料夾不存在, 才建立資料夾
if not os.path.isdir(base_dir):
    os.mkdir(base_dir)

for i in range(len(classes)):
    # 分拆成訓練、驗證與測試資料夾
    switch = True
    for j in range(len(sets)):
        file_path_1 = os.path.join(base_dir, sets[j])
        if not os.path.isdir(file_path_1):
            os.mkdir(file_path_1)
        file_path_2 = os.path.join(file_path_1, classes[i])
        if not os.path.isdir(file_path_2):
            os.mkdir(file_path_2)
        # 查詢單一種類樣本數量
        if switch:
            dirPathPattern = os.path.join(
                original_dataset_dir, str(classes[i] + '*'))
            result = glob.glob(dirPathPattern)
            switch = False
        sample_number = int(len(result)*dataset_percent[j])
        # print(sample_number)
        # 從資料集隨機抽樣
        filePaths = random.sample(result, sample_number)
        result = set(result)-set(filePaths)
        result = list(result)
        # 將圖片複製到指定之資料夾
        for filePath in filePaths:
            fname = os.path.basename(filePath) 
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(file_path_2, fname)
            shutil.copyfile(src, dst)
        print(classes[i], sets[j],len(os.listdir(file_path_2)))
print('finish!')

import numpy as np

def main(userFilePath, tagListPath):
    with open(tagListPath, 'r') as tagListFile:
        jsonData = json.load(tagListFile)
        tagList = jsonData['tag_list']

    userVector = np.zeros(tagList.length, 1)
    with open(userFilePath, 'r') as userFile:
        jsonUser = json.load(userFile)
        for tag in jsonUser:
            userVector[tagList.index(tag)] = jsonUser[tag]

    vectorFilePath = 'userVector.json'
    with open(vectorFilePath, 'w') as vectorFile:
        json.dump({'userVector':userVector.tolist()},vectorFile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Makes a vector of listened tags')
    parser.add_argument('userFile', help='json file of tag srobbles')
    parser.add_argument('tagList', help='sorted json file with all tag')
    args = parser.parse_args()
    main(args.userFile, args.tagList)

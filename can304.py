def keyGeneration(plaintext):
    # Step1: Generate a random key of any size
    print("Start keyGeneration using ", plaintext)
    # Step2:Find the ASCII value of each character of the key
    ascii_list = []
    for i in range(len(plaintext)):
        ascii_list.append(ord(plaintext[i]))
    print("ASCII value list of plaintext is: ", ascii_list)
    # Step3: Find the smallest value from the ASCII values of the key
    lowest_ascii_value = min(ascii_list)
    print("The lowest value of plaintext is: ", lowest_ascii_value)
    # Step4: Perform the mod operation on each ASCII value
    mod_list = []
    for i in ascii_list:
        mod_list.append(i % lowest_ascii_value)
    print("Mod list is: ", mod_list)
    # Step5: Find the largest value from step 2 and XOR it with the value obtained from step 4
    largest_ascii_value = max(ascii_list)
    print("Largest ASCII Value is: ", largest_ascii_value)
    xor_list = []
    for i in mod_list:
        xor_list.append(largest_ascii_value ^ i)
    print("xor list is: ", xor_list)
    # Step6: Add value from step 3 into the value calculated by step 5
    add_smlt = []
    for i in xor_list:
        add_smlt.append(i+lowest_ascii_value)
    print("Add smlt list is:", add_smlt)
    # Step7: Final Key Generation, Add_smlt Mod 13
    final_key_list = []
    for i in add_smlt:
        final_key_list.append(i % 13)
    print("Final key list is: ", final_key_list)
    return final_key_list


def rot13(message):
    first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    trantab = str.maketrans(first, trance)
    return message.translate(trantab)

def encryption(plaintext,key):
    # Step 0: Generate Key Table
    final_key_list = keyGeneration(key)
    print("Key generation Finished!!!!")
    # Step1: Input the plain text
    print("The plaintext is: ", plaintext, " start to encryption!")
    # Step2: Apply ROT13 to the plain text
    rot13_text = rot13(plaintext)
    print("The ROT text is: ", rot13_text)
    # Step3: Find the ASCII value of each character of step 2.
    ascii_list = []
    for i in range(len(rot13_text)):
        ascii_list.append(ord(rot13_text[i]))
    print("ASCII value list of ROT text is: ", ascii_list)
    # Step4: Find the lowest ASCII value from the data.
    lowest_ascii_value = min(ascii_list)
    print("The lowest value of the ROT text is: ", lowest_ascii_value)
    # Step5: Perform mod operation on each ASCII value obtained from step 4 with the lowest value.
    mod_list = []
    for i in ascii_list:
        mod_list.append(i % lowest_ascii_value)
    print("Mod list is: ", mod_list)
    # Step6: XOR the key with the data calculated in step 5.

    xor_with_FK_list = []
    # if len(mod_list) <= len(final_key_list):
    #     for i in range(len(mod_list)):
    #         xor_with_FK_list.append(final_key_list[i] ^ mod_list[i])
    #         #xor_with_FK_list.append(final_key_list[i % len(final_key_list)] ^ mod_list[i])
    # else:
    #     round=0
    for i in range(len(mod_list)):
            # if i == len(final_key_list):
            #     round=round+1
            # xor_with_FK_list.append(final_key_list[i-round*len(final_key_list)] ^ mod_list[i])
        xor_with_FK_list.append(final_key_list[i % len(final_key_list)] ^ mod_list[i])

    print("xor_with_FK_list is: ",xor_with_FK_list)

    # Step7: Perform mod 13 on the values calculated by step 6.
    # Step8: Save the quotient achieved from step 7 for decryption.
    quotient_list = []
    mod13_list = []
    for i in xor_with_FK_list:
        quotient_list.append(int(i / 13))
        mod13_list.append(i % 13)
    print("Q is: ",quotient_list)
    print("Mod13 is: ",mod13_list)
    # Step9: Add the smallest value of step 4 in the text obtained from step 8.
    addsmlt = []
    for i in mod13_list:
        addsmlt.append(i + lowest_ascii_value)
    print("addsmlt is : ",addsmlt)
    # Step10: Convert the values into characters so that cipher text is achieved.
    chr_list= []
    for i in addsmlt:
        chr_list.append(chr(i))
    print("Cipher.T is :",chr_list)
    # Step11: Make final encrypted data by scrambling cipher text and quotients at the alternate bits
    final_list= []
    for i in range(len(quotient_list)):
        final_list.append(chr_list[i])
        final_list.append(str(quotient_list[i]))
    cipher = "".join(final_list)
    print(cipher)
    return cipher

def decryption(encrypteddata, key):
    final_key_list=keyGeneration(key)
    print("final key lit is: ", final_key_list)
    # Step1 Take the final encrypted data
    print("The final encrypted data is: ", encrypteddata)

    # Step2 Remove the quotinets from the final encrypted
    tolist = list(encrypteddata)
    encrypteddata_list= []
    quotient_list = []
    for i in range(len(tolist)):
        if i % 2==0:
            encrypteddata_list.append(tolist[i])
        else:
            quotient_list.append(tolist[i])
    print("encrypteddata_list is: ",encrypteddata_list)
    print("quotient_list is:",quotient_list)

    # Step3 Find the ASCII value of each character of the cipher text
    ascii_list = []
    for i in range(len(encrypteddata_list)):
        ascii_list.append(ord(encrypteddata_list[i]))
    print("ASCII value list of encrypteddata_list is: ", ascii_list)

    # Step4 Find the smallest value from step 2 and subtract it
    lowest_ascii_value = min(ascii_list)
    print("The lowest value of encrypteddata is: ", lowest_ascii_value)
    subsmlt_list = []
    for i in ascii_list:
        subsmlt_list.append(i-lowest_ascii_value)
    print("Sub smlt is: ", subsmlt_list)

    # Step5 Multiply the value of quotient with 13 and add to step 3
    q13subsmlt_list = []
    for i in range(len(subsmlt_list)):
        q13subsmlt_list.append(subsmlt_list[i] + 13 * int(quotient_list[i]))
    print("(13 * Q) + Sub smlt list is: ", q13subsmlt_list)

    # Step6 Perform XOR operation on the resultant of step 4 with the key
    xor_with_FK_list = []
    if len(q13subsmlt_list) <= len(final_key_list):
        for i in range(len(q13subsmlt_list)):
            xor_with_FK_list.append(final_key_list[i] ^ q13subsmlt_list[i])
    else:
        round = 0
        for i in range(len(q13subsmlt_list)):
            # if i == len(final_key_list):
            #     round = round + 1
            # xor_with_FK_list.append(final_key_list[i - round * len(final_key_list)] ^ q13subsmlt_list[i])
            xor_with_FK_list.append(final_key_list[i % len(final_key_list)] ^ q13subsmlt_list[i])

    print("xor_with_FK_list is: ", xor_with_FK_list)
    # Step7 Add the smallest value calculated from step 3 to the resultant of step 6
    addsmlt_list = []
    for i in range(len(xor_with_FK_list)):
        addsmlt_list.append(lowest_ascii_value + xor_with_FK_list[i])
    print("Add smlt is :", addsmlt_list)
    # Step8 Convert ASCII values into characters
    chr_list = []
    for i in addsmlt_list:
        chr_list.append(chr(i))
    chr_str="".join(chr_list)
    print("Rot 13 text is :", chr_str)
    # Step9 Appling ROT 13 to the characters obtained in step 7
    plaintext = rot13(chr_str)
    print("The plaintext is: ", plaintext)
    # Step10 Plain text is achieved
    return plaintext

if __name__ == '__main__':

    cipher = encryption("AppleWeAreProudToBePakistaniAlgorithm","Crypto")
    cipher = encryption("HeoBob","Crypto")
    plaintext = decryption(cipher,"Crypto")
    #print("After decryption, the plaintext is: ", plaintext)

#"D0N2K0F3O2L0M2K1O2O2C1L1M0N2F0L2K4I4N2J3D3L1I4"

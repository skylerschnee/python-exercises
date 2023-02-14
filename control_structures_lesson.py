{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "beb72288",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'coffee'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "breakfast = 'coffee'\n",
    "breakfast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "aa6675c7",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "EOL while scanning string literal (2094139656.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Input \u001b[0;32mIn [2]\u001b[0;36m\u001b[0m\n\u001b[0;31m    print ('you had fruit!)\u001b[0m\n\u001b[0m                           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m EOL while scanning string literal\n"
     ]
    }
   ],
   "source": [
    "if breakfast == 'banana':\n",
    "    print ('you had fruit!)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dac00084",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you had fruit!\n"
     ]
    }
   ],
   "source": [
    "if breakfast == 'banana':\n",
    "    print('you had fruit!')\n",
    "else:\n",
    "    print('you had something else? Nothing? IDK!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7b9375d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "breakfast = 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e0bbfaa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(breakfast)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b1ea3dff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "banana\n"
     ]
    }
   ],
   "source": [
    "print(breakfast)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "23553e80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "thats a string value\n",
      "thats fruit\n"
     ]
    }
   ],
   "source": [
    "#nesting\n",
    "\n",
    "if type(breakfast) == str:\n",
    "    print('thats a string value')\n",
    "    if breakfast in ['banana', 'orange']:\n",
    "        print('thats fruit')\n",
    "    else:\n",
    "        print('thats something else')\n",
    "else:\n",
    "    print ('thats not a string')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf6d3c1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# strings as list-like things"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f28262b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# is 'a' in banana?\n",
    "\n",
    "'a' in 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "de718297",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# is 'z' in banana?\n",
    "\n",
    "'z' in 'banana'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "de1aec5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'banana'[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "00e2632d",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_other_gwen_list = [let + '!' for let in 'bananas']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cf8e5a5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "### LOOPS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "66f407a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for i in itr:\n",
    "#    do action, probably relating to i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1feba80f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b\n",
      "a\n",
      "n\n",
      "a\n",
      "n\n",
      "a\n",
      "s\n"
     ]
    }
   ],
   "source": [
    "gwen_list = []\n",
    "for i in 'bananas':\n",
    "    print(i)\n",
    "    gwen_list.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7288e3f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b', 'a', 'n', 'a', 'n', 'a', 's']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gwen_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0463609f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b!', 'a!', 'n!', 'a!', 'n!', 'a!', 's!']"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_other_gwen_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fcf79d0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# remember: '+' works both to concatenate as well as add, contigent on the data type "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9e019e91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'4ba'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4 + 'ba' will not work. But you can concat like this:\n",
    "\n",
    "str(4) + 'ba'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e9eed2fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type a number 8\n"
     ]
    }
   ],
   "source": [
    "my_number = input('type a number ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "7085c112",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# my_number > 5 #does not work because input() defaults as a string\n",
    "\n",
    "#try this\n",
    "\n",
    "int(my_number) > 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c37b8deb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Object `lower` not found.\n"
     ]
    }
   ],
   "source": [
    ".lower?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "35681dd7",
   "metadata": {},
   "outputs": [],
   "source": [
    ".my_number?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "4bcd4d06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi! ef\n",
      "hi! ef\n",
      "hi! e\n",
      "hi! f\n",
      "hi! efe\n",
      "i dont have all day\n"
     ]
    }
   ],
   "source": [
    "# annoym\n",
    "\n",
    "\n",
    "response = ''\n",
    "counter = 0\n",
    "while response != 'stop_please':\n",
    "    response = input('hi! ')\n",
    "    counter += 1\n",
    "    if counter >=5:\n",
    "        print('i dont have all day')\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a01da5db",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bd1b79d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

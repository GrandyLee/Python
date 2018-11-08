import pickle
my_list=[123,3.14,'小小龙',['another list']]
pickle_file=open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
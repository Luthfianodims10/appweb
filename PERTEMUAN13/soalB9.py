import pickle
filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))
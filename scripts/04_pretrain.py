import seisnn

dataset = 'HL2019'
model_instance = 'test_model'
database = 'HL2019.db'

trainer = seisnn.model.trainer.GeneratorTrainer(database)
trainer.train_loop(dataset, model_instance, plot=True, remove=True)

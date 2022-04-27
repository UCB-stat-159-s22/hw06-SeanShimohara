from readligo import loaddata 

def test_loaddata:
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/"+fn_H1, 'H1')
	assert len(time_H1) == 131072
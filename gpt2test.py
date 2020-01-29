import gpt_2_simple as gpt2 

gpt2.download_gpt2()
sess = gpt2.start_tf_sess()
gpt2.finetune(sess, 'sampletext.txt', steps=1000)

sampletext = gpt2.generate(sess)

f = open('gpt2generated.txt', 'w')
f.write(sampletext)
f.close()
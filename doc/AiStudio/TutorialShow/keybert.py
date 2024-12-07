from sklearn.feature_extraction.text import CountVectorizer
import jieba
from keybert import KeyBERT

def tokenize_zh(text):
    words = jieba.lcut(text)
    return words

vectorizer = CountVectorizer(tokenizer=tokenize_zh)
kw_model = KeyBERT()

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal). 
         A supervised learning algorithm analyzes the training data and produces an inferred function, 
         which can be used for mapping new examples. An optimal scenario will allow for the 
         algorithm to correctly determine the class labels for unseen instances. This requires 
         the learning algorithm to generalize from the training data to unseen situations in a 
         'reasonable' way (see inductive bias).
      """

doc_cn = """
* 当单机没有足够GPU,多机足够时，选择“非分布式训练”。平台进行调度，但一直调度不成功。希望此时提示用户单机卡不足够，应选择“分布式训练”
* 你们遇到是CPU,MEM利用不起来，还是个别训练任务CPU,MEM使用量奇高？你们现在开发或训练任务使用CPU，或内存有没有一些经验值，现在可以做全局的使用上限限制？
    - 内存这个主要还是看数据集，cpu需求主要看数据增强了，这个真不好给所有任务一个具体限制。  按照我以前用的平台经验，1 cpu对应10g内存，一般申请8-15cpu
    - 我们不同的任务，数据集大小不同。像我这边处理视频的话，就是有多少用多少，当然会限制dataloader的长度。我目前在跑的任务，一般来说num_worker=0的时候， 能够让GPU高效利用起来的batch_size只有16
* 2021-0922 【pengfei】有2个节点的卡用用户自己保存的image起GPU任务，报错： ImagePullBackOFF！ 
    - 这2个节点是他人任务结束后释放出来，已经在集群中，但是该节点的harbor host配置丢失，不能访问集群内的harbor
* 2021-0922 【pengfei】创建的模型训练任务，偶现没有日志打印；
    - 在后台进入pod查看有训练日志，但是WEB没有输出 
* 2021-0922 【yingying】启动文件为软链接时，报错找不到启动文件
    - 软连接的启动脚本在linux终端是可以执行，但是在平台创建训练任务窗口则报文件找不到
    """

keywords = kw_model.extract_keywords(doc, vectorizer=vectorizer)
print("======>", keywords)

将虚拟环境添加到jupyterLba
1. pip install ipykernel
2. 在当前虚拟环境(myenv)执行添加命令
python -m ipykernel install --user --name=myenv
3. 列举已添加的环境
jupyter kernelspec list
4. 卸载已添加的环境
jupyter kernelspec uninstall myenv
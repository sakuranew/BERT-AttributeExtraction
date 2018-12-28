
# BERT-Attribute-Extraction
##  基于bert的知识图谱属性抽取
USING BERT FOR Attribute Extraction in KnowledgeGraph with two method,fine-tuning and feature extraction.
 
知识图谱百度百科人物词条属性抽取，使用基于bert的微调fine-tuning和特征提取feature-extraction方法进行实验。


### Prerequisites


```
Tensorflow >=1.10
scikit-learn
```
### Pre-trained models
 **[`BERT-Base, Chinese`](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)**:
    Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M
    parameters
    
### Installing

None
## Dataset

The dataset is constructed according to Baidu Encyclopedia character entries.
Filter out corpus that does not contain entities and attributes.

Entities and attributes are  obtained from name entity recognition.

Labels are  obtained from the  Baidu Encyclopedia infobox, and most of them are labeled manually,so some are not very good.  
For example:
    
    黄维#1904年#1#黄维（1904年-1989年），字悟我，出生于江西贵溪一农户家庭。        
    陈昂#山东省滕州市#1#邀请担任诗词嘉宾。1992年1月26日，陈昂出生于山东省滕州市一个普通的知识分子家庭，其祖父、父亲都
    陈伟庆#肇庆市鼎湖区#0#长。任免信息2016年10月21日下午，肇庆市鼎湖区八届人大一次会议胜利闭幕。陈伟庆当选区人民政府副区长。
## Getting Started

* run `strip.py` can get striped data
* run `data_process.py` can process data to get numpy file input
* `parameters` file is the parameters that run model need

## Running the tests

For example with birthplace dataset：
    
* fine-tuning
    * run `run_classifier.py` to get predicted probability outputs
    ```shell
    python run_classifier.py \
            --task_name=my \
            --do_train=true \
            --do_predict=true \
            --data_dir=a \
            --vocab_file=/home/tiny/zhaomeng/bertmodel/vocab.txt \
            --bert_config_file=/home/tiny/zhaomeng/bertmodel/bert_config.json \
            --init_checkpoint=/home/tiny/zhaomeng/bertmodel/bert_model.ckpt \
            --max_seq_length=80 \
            --train_batch_size=32 \
            --learning_rate=2e-5 \
            --num_train_epochs=1.0 \
            --output_dir=./output
    ```    
    * then run `proba2metrics.py` to get final result with wrong classification

* feature-extraction
    * run `extract_features.py` to get the vector representation of train and test data in json file format
    ```shell
    python extract_features.py \
            --input_file=../data/birth_place_train.txt \
            --output_file=../data/birth_place_train.jsonl \
            --vocab_file=/home/tiny/zhaomeng/bertmodel/vocab.txt \
            --bert_config_file=/home/tiny/zhaomeng/bertmodel/bert_config.json \
            --init_checkpoint=/home/tiny/zhaomeng/bertmodel/bert_model.ckpt \
            --layers=-1 \
            --max_seq_length=80 \
            --batch_size=16
    ```    
    * then run `json2vector.py` to transfer json file to vector representation
    * finally run `run_classifier.py` to use machine learning methods to do classification,MLP usually peforms best 

## Result
The predicted results and misclassified corpus are saved in result dir.
* For example with birthplace dataset using fine-tuning method,the result is:    

                  precision    recall  f1-score   support

           0      0.963     0.967     0.965       573
           1      0.951     0.946     0.948       389
## Authors

* **zhao meng** 
## License

This project is licensed under the MIT License 

## Acknowledgments

* etc

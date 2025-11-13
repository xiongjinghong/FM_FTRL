# FM_FTRL
Hashed Factorization Machine with Follow The Regularized Leader online learning for Kaggle Avazu Click-Through Rate Competition

Based on Tinrtgu's code at: http://www.kaggle.com/c/avazu-ctr-prediction/forums/t/10927/beat-the-benchmark-with-less-than-1mb-of-memory   

data: https://www.kaggle.com/c/avazu-ctr-prediction/discussion/10927

data: https://tianchi.aliyun.com/dataset/147617



Features:
- online learning
- feature hashing to limit memory footprint
- Follow the Regularized Leader (FTRL) optimization: http://research.google.com/pubs/pub41159.html
- Factorization Machine (low rank matrix factorization)
- L1 and L2 regularization
- dropout regularization option


Run fast with pypy:

    pypy runmodel_example.py


or run slow with regular python:

    python runmodel_example.py



#コンテナのベースイメージとしてubuntu:20.04を設定
FROM ubuntu:22.04

#環境変数設定
ENV TZ=Asia/Tokyo 
ENV DEBIAN_FRONTEND noninteractive

#aptのアップデート確認とアップデートの実施+Python3のインストール+Python3で利用するモジュール等のインストール
RUN apt update && apt install -y \
    tzdata \
    wget \
    build-essential \
    libbz2-dev libdb-dev \
    libreadline-dev libffi-dev \
    libgdbm-dev \
    liblzma-dev \
    libncursesw5-dev \
    libsqlite3-dev \
    libssl-dev \
    zlib1g-dev uuid-dev \
    tk-dev

#Pythonのビルド
RUN mkdir temp && \
    cd temp && \
    wget https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tar.xz && \
    tar xJf Python-3.11.8.tar.xz && \
    cd Python-3.11.8 && \
    ./configure && \
    make && \
    make install &&\
    cd .. &&\
    rm -rf temp

#Pythonモジュールのインストール
COPY requirements.txt sample_streamlit.py ./
RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt-get/lists/*

ENTRYPOINT ["streamlit"]
CMD ["run", "sample_streamlit.py", "--server.port", "5678"]
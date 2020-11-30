FROM elytra8/projectfizilion:latest

RUN mkdir /Fizilion && chmod 777 /Fizilion
ENV PATH="/Fizilion/bin:$PATH"
WORKDIR /Fizilion

RUN git clone https://github.com/FrosT2k5/ProjectFizilion -b dragon /Fizilion

RUN pip3 install google_trans_new
#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /Fizilion/
#transfer

RUN curl -sL https://git.io/file-transfer | sh

#
# Finalization
#
CMD ["python3","-m","userbot"]

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:30:27 2018

@author: Steff
@author: Andreea
"""

import os
from gensim.models.keyedvectors import KeyedVectors
import spacy
import numpy as np

class EmbeddingsParser:

    path_pretrained_embeddings = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "..",
            "data",
            "external"
    )

    path_embeddings = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "..",
            "data",
            "processed",
            "word_embeddings"
    )

    
    paths = {
            "6d50":os.path.join(path_pretrained_embeddings,"glove.6B.50d.txt"),
            "6d50-w2v":os.path.join(path_pretrained_embeddings,"glove.6B.50d-w2v.txt"),
            "6d50-folder":os.path.join(path_pretrained_embeddings,"glove.6B.50d-spacy",""),
            "6d100":os.path.join(path_pretrained_embeddings,"glove.6B.100d.txt"),
            "6d100-w2v":os.path.join(path_pretrained_embeddings,"glove.6B.100d-w2v.txt"),
            "6d100-folder":os.path.join(path_pretrained_embeddings,"glove.6B.100d-spacy",""),
            "6d200":os.path.join(path_pretrained_embeddings,"glove.6B.200d.txt"),
            "6d200-w2v":os.path.join(path_pretrained_embeddings,"glove.6B.200d-w2v.txt"),
            "6d200-folder":os.path.join(path_pretrained_embeddings,"glove.6B.200d-spacy",""),
            "6d300":os.path.join(path_pretrained_embeddings,"glove.6B.300d.txt"),
            "6d300-w2v":os.path.join(path_pretrained_embeddings,"glove.6B.300d-w2v.txt"),
            "6d300-folder":os.path.join(path_pretrained_embeddings,"glove.6B.300d-spacy",""),
            "42d300":os.path.join(path_pretrained_embeddings,"glove.42B.300d.txt"),
            "42d300-w2v":os.path.join(path_pretrained_embeddings,"glove.42B.300d-w2v.txt"),
            "42d300-folder":os.path.join(path_pretrained_embeddings,"glove.42B.300d-spacy",""),
            "840d300":os.path.join(path_pretrained_embeddings,"glove.840B.300d.txt"),
            "840d300-w2v":os.path.join(path_pretrained_embeddings,"glove.840B.300d-w2v.txt"),
            "840d300-folder":os.path.join(path_pretrained_embeddings,"glove.840B.300d-spacy",""),
            "word2vec-w2v":os.path.join(path_pretrained_embeddings,"GoogleNews-vectors-negative300.bin"),
            "word2vec-folder":os.path.join(path_pretrained_embeddings,"word2vec-spacy",""),
            "fasttext-w2v": os.path.join(path_pretrained_embeddings, "wiki-news-300d-1M.vec"),
            "fasttext-folder":os.path.join(path_pretrained_embeddings, "fasttext-spacy",""),
            "w2v_50d_w5_CBOW_HS-w2v":os.path.join(path_embeddings, "w2v_50d_w5_CBOW_HS.bin"),
            "w2v_50d_w5_CBOW_HS-folder":os.path.join(path_embeddings, "w2v_50d_w5_CBOW_HS-spacy",""),
            "w2v_50d_w5_CBOW_NS-w2v":os.path.join(path_embeddings, "w2v_50d_w5_CBOW_NS.bin"),
            "w2v_50d_w5_CBOW_NS-folder":os.path.join(path_embeddings, "w2v_50d_w5_CBOW_NS-spacy",""),
            "w2v_50d_w10_SG_HS-w2v":os.path.join(path_embeddings, "w2v_50d_w10_SG_HS.bin"),
            "w2v_50d_w10_SG_HS-folder":os.path.join(path_embeddings, "w2v_50d_w10_SG_HS-spacy",""),
            "w2v_50d_w10_SG_NS-w2v":os.path.join(path_embeddings, "w2v_50d_w10_SG_NS.bin"),
            "w2v_50d_w10_SG_NS-folder":os.path.join(path_embeddings, "w2v_50d_w10_SG_NS-spacy","")
            
    }
    
    lengths = {
            "6d50":50,
            "6d100":100,
            "6d200":200,
            "6d300":300,
            "42d300":300,
            "840d300":300,
            "word2vec":300,
            "fasttext": 300,
            "w2v_50d_w5_CBOW_HS":50,
            "w2v_50d_w5_CBOW_NS":50,
            "w2v_50d_w10_SG_HS":50,
            "w2v_50d_w10_SG_NS":50,
    }
    
    models = {}
    
    nlp = spacy.load("en",vectors=False)
        
    def load_model(self, model, pretrained = True):
        """
        Loads a pre-trained word embedding to be used by this parser.
        
        Args:
            model (str): The model used. 
                One of pretrained {"6d50","6d100","6d200","6d300","42d300","840d300", "word2vec", "fasttext"}.
                One of the models trained on the abstracts' text data.
            
            pretrained(bool): Whether the used embeddings are pretrained or not.
        """
        try:
            self.nlp = spacy.load(self.paths[model + "-folder"])
            self.length = self.lengths[model]
            
        except OSError:
            if not os.path.isfile(self.paths[model + "-w2v"]) and pretrained:
                from gensim.scripts.glove2word2vec import glove2word2vec
                print("Word2Vec format not present, generating it.")
                glove2word2vec(glove_input_file=self.paths[model], word2vec_output_file=self.paths[model + "-w2v"])
                        
            try:
                self.current_model = self.models[model + "-w2v"]
                self.length = self.lengths[model]
            except KeyError:
                if pretrained:
                    if model == "fasttext":
                        print("FastText not loaded yet, loading it.")
                        binary = False
                    elif model == "word2vec":
                        print("Word2Vec not loaded yet, loading it.")
                        binary = True
                    else:
                        print("Glove not loaded yet, loading it.")
                        binary = False
                else:
                    print("Pretrained model not loaded yet, loading it.")
                    binary = True
                
                self.models[model + "-w2v"] = KeyedVectors.load_word2vec_format(self.paths[model + "-w2v"], binary=binary)             
                self.current_model = self.models[model + "-w2v"]
                self.length = self.lengths[model]
            
            print("Setting up spacy vocab.")
            
            count = 0
            for word, o in self.current_model.vocab.items():
                count += 1
                self.nlp.vocab.set_vector(word, self.current_model[word])
            
            print("Done ({}). Saving to disk.".format(count))
            
            try:
                self.nlp.to_disk(self.paths[model + "-folder"])
            except FileNotFoundError:
                os.mkdir(self.paths[model + "-folder"])
                self.nlp.to_disk(self.paths[model + "-folder"])
    
    #################################################    
    def transform_matrix(self,sentence):
        """
        Transform a string into a matrix containing word embeddings as rows.
        
        Args:
            sentence (str): The string to be transformed. Can be a sentence or a whole document.
            
        Returns:
            A numpy matrix that contains word embeddings as rows of each word given by "sentence".
        """
        for w in self.nlp(sentence):
            try:
                m = np.concatenate((m,[w.vector]),axis=0)
            except NameError:
                m = np.array([w.vector])
            
        return m
    
    #################################################
    def transform_vector(self,sentence):
        """
        Transform a string into a vector containing concatenated word embeddings.
        
        Args:
            sentence (str): The string to be transformed. Can be a sentence or a whole document.
            
        Returns:
            A numpy array that contains concatenated word embeddings for each word given by "sentence".
        """
        
        for w in self.nlp(sentence):
            try:
                m = np.append(m,w.vector)
            except NameError:
                m = np.array(w.vector)
            
        return m
    
    #################################################
    def transform_vectors(self,sentences,batch_size=100):
        """
        Transform a list of strings into a list of vectors containing concatenated word embeddings.
        
        Args:
            sentence list(str): The list of strings to be transformed.
            
        Returns:
            A list of numpy arrays that contain concatenated word embeddings for each word given by "sentence".
        """
        
        vectors = list()
        for doc in self.nlp.tokenizer.pipe(sentences, batch_size=batch_size):
            m = np.empty(len(doc)*self.length)
            for i, w in enumerate(doc):
                m[(i*self.length):((i+1)*self.length)] = w.vector
            vectors.append(m)
            
        return vectors
    
    #################################################
    def transform_avg_vectors(self,sentences,batch_size=100):
        """
        Transform a list of strings into a list of vectors containing averaged word embeddings.
        
        Args:
            sentence list(str): The list of strings to be transformed.
            
        Returns:
            A list of numpy arrays that contain averaged word embeddings for each word given by "sentence".
        """
        
        vectors = list()
        for doc in self.nlp.tokenizer.pipe(sentences, batch_size=batch_size):
            m = np.empty(self.length)
            for i, w in enumerate(doc):
                m = np.add(m,w.vector)
            vectors.append(m/len(doc))
            
        return vectors
    
    
        
## Example:
#parser = EmbeddingsParser()
#parser.load_model("6d50")
#test = parser.transform_vector("oi mate, what's going on?")
#print(test.shape)
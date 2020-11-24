# x-rhythm-can: Creative-GAN for Novel Rhythm Generation


<img src="https://cclab.sfc.keio.ac.jp/wp-content/uploads/2020/07/can_framework-1024x426.png" width="512" height="213" />

**Creative Adversarial Network for generating novel Dance Music Rhythm Patterns**
  
***Can we use AI, more specifically GAN, to originate new electronic dance music genres?***
  
> Since the introduction of deep learning, researchers have proposed content generation systems using deep learning and proved that they are competent to generate convincing content and artistic output, including music. However, one can argue that these deep learning-based systems imitate and reproduce the patterns inherent within what humans have created, instead of generating something new and creative.   
In this paper, we focus on music generation, especially rhythm patterns of electronic dance music, and discuss if we can use deep learning to generate novel rhythms, interesting patterns not found in the training dataset.
We extend the framework of Generative Adversarial Networks(GAN) and encourage it to diverge from the inherent distributions in the dataset by adding additional classifiers to the framework. The paper shows that our proposed GAN can generate rhythm patterns that sound like music rhythms but not belong to any genre in the training dataset.  


# Project Page
https://cclab.sfc.keio.ac.jp/projects/rhythmcan/


# Requirements

Before doing `pip install -r requirements.txt`, edit `requirements.txt` depending on your needs please.

- Python 3.6 or later
- TensorFlow (tested with 1.15.1)
- keras 
- matplotlib
- pyfluidsynth etc.

also, you need to install `fluidsynth` separately by `sudo apt-get install fluidsynth`.


    
# Generated Rhythms

You can find generated samples of *Conditional-GAN* and *Creative-GAN* in `./audio_samples/` directory. 

Or here are soundcloud playlists:  
[Creative-GAN rhythm patterns](https://soundcloud.com/deeplearning-music/sets/generated-by-creative-gan-gan-with-genre-ambiguity-loss)  
[Conditional-GAN rhythm patterns](https://soundcloud.com/deeplearning-music/sets/rhythm-patterns-generated-by-genre-conditioned-gan)
  
   

# Training


# Reference

We got the inspiration from the following paper: 

> Elgammal, Ahmed, Bingchen Liu, Mohamed Elhoseiny, and Marian Mazzone. “CAN: Creative Adversarial Networks, Generating "Art" by Learning About Styles and Deviating from Style Norms,” June 21, 2017. http://arxiv.org/abs/1706.07068.

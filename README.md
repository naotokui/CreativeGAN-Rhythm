# x-rhythm-can
Creative Adversarial Network for generating novel Dance Music Rhythm Patterns


![Creative-GAN arthitecture](https://cclab.sfc.keio.ac.jp/wp-content/uploads/2020/07/can_framework-1024x426.png "Creative-GAN arthitecture")




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

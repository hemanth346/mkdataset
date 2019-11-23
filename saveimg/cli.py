import click
import os
from saveimg.generate import GenerateData
from saveimg.exceptions import FailedValidation

@click.command()
@click.argument('name')

@click.option('--directory', '-d', 
                default='.', 
                type= click.Path(writable=True, resolve_path=True),
                help='Directory where images has to be saved, expects path not string'
                )

@click.option('--video', '-v', 
                default=0,
                type = click.File(),
                help='Video file to parse, default is webCam feed'
                )

@click.option('--fps', '-s', 
                default=1, 
                help='Capture rate in seconds per Frame'
                )

@click.option('--distribution', '-p', 
                default=(0.6, 0.2, 0.2), 
                help='Distribution of train, test and valid images to be saved'
                )

@click.option( '--cont', '-c',
                default=False,
                type = click.BOOL,
                help='If train, test and validation images should have continuity in naming'
                )

@click.option('--reverse', '-r', 
                default='no',
                type = click.BOOL,
                help='If train, test and validation should be inside class folder unlike class folder inside these'
                )

def save(name, directory, fps, distribution, video, reverse, cont):
    '''
    Capture frame from video feed at set intervals
    and save them as an organized dataset with 
    images in training, test and validation folders
    
    Currently supports only for one class name

    '''
    print('-'*81)
    print("\tDirectory is {}".format(directory))
    print("\n\tSaving image every {} seconds".format(fps))
    print("\n\tSaving train, test and validation in ratio of {}".format(distribution))
    print("\n\tReading video feed from {}".format(video.name if video.name else 'Webcam'))
    print('-'*81)

    proceed = click.prompt("Please enter to proceed : ", 
        default=True,
        type = bool,
    )
    if proceed:
        feed = GenerateData(name, path=directory, reverse=reverse, continuous=cont, distribution=distribution)
        video = video if video.name else 0
        feed.capture(file=video, fps=fps)
    else:
        # exit(1)
        raise FailedValidation("Exiting due to failed user validation")

save()

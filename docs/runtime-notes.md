# Runtime notes

These notes describe limitations observed in the preserved teaching source. They are separate from the original tutorials.

## Historical environments

- Keras, FastAI, TensorFlow Object Detection and ML.NET examples use historical dependencies or API conventions.
- The ML.NET project targets .NET Core 2.2 in its project metadata.
- Some tutorial requirements files are empty or incomplete; they do not define a tested modern environment.
- Hosting and external-provider instructions are retained as historical references. Their present availability and pricing were not verified.

No claim is made that all examples run under current libraries. Tutorial programs were not executed as part of the structural cleanup.

## Machine-specific paths

The ensemble-learning notebook includes an original author-specific `C:/Users/.../Datasets` location. It must be changed to a local copy of the required dataset before running.

The TensorFlow surveillance scripts append original machine-specific paths for `research/slim` and `research/object_detection`. Those paths must point to a locally installed TensorFlow Models checkout. The checkout is not included.

## Relative resources

Topic folders retain their internal layout. Run a script or start Jupyter from the directory that contains its local input assets. This keeps its existing relative dataset/model references meaningful.

## Source links

Original badges, article references and links to the author's repositories remain attributed upstream. The root catalog points to this fork's reorganized folders.

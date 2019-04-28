class Post(object):
    POST_TYPES = {1: "Text", 2: "Image", 3: "Video", 4: "Link"}

    """Post is anything user or company posts in their timeline.

    
    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        POST_TYPES (list): Types of post like image video text, links

    """

    def __init__(self, type_of):
        """

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            type (str): type of post.

        """
        self.type = type_of


    @property
    def type_display(self):
        """str: Display type of post type in string"""
        return self.POST_TYPES[self.type]

    def post_text(self, text):
        """A post of type text.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            text: Text of a post.

        Returns:
            True if successful, False otherwise.

        """
        if text:
            self.text = text
            return True
        return False

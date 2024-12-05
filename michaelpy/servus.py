from emoji import emojize

def servus(name = "world"):
  """Servus
  
  This function will great you in a bavarian way.
  
  Parameters
  ----------
  name : str
    The name of the person to be greated.

  Returns
  -------
  str:
    Bavarian greating.
  
  Examples
  --------
  >>> print(servus("Hias"))
  >>> Servus Hias! ....
  """
  return emojize(f"Servus {name}! Welcome to my first Python package! :thumbs_up:")
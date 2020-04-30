function wordMapForArticles()
{
    var words;
    if(this.Article_Content != null)
    {
        words = this.Article_Content.toLowerCase().match(/\w+/gi);
    }

    if(words == null)
    {
        return;
    }

    for(var i=0; i<words.length; i++)
    {
        emit(words[i], {count:1});
    }

}
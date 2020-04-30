function wordMapForMultipleWords()
{

    var multiplewords;
    if(this.Article_Content != null)
    {
        multiplewords = this.Article_Content.toLowerCase().match(/(\w)+ (\w)+/gi);
    }
    if(multiplewords == null)
    {
        return;
    }

    for(var i=0; i<multiplewords.length; i++)
    {
        emit(multiplewords[i], {count:1});
    }

}
function wordMapForMultipleWords()
{
    var multiplewords = this.Tweet_Text.toLowerCase().match(/(\w)+ (\w)+/gi);

    if(multiplewords == null)
    {
        return;
    }

    for(var i=0; i<multiplewords.length; i++)
    {
        emit(multiplewords[i], {count:1});
    }

}
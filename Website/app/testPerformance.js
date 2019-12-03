describe('Test for Performance on Suggestions', function() {

  describe('Google Form Time', function () {
    it('The google form should take less than 5 ms and be fully loaded', function () {
      var document = "suggestions.html";
      var str = "*forms.gle";
      obj = document.NativeWebObject.Find("innerHTML", str);
      if (obj.Exists)
        Log.Message("Object containing text '" + str + "' is found", obj.FullName);
      else
        Log.Warning("Object containing text '" + str + "' was not found.");

  });
  });
});
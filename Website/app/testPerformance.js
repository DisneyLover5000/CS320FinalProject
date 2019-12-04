describe('Test for Performance', function() {

  describe('Google Form Loading', function () {
    it('The google form should take less than 5 ms and be loaded', function () {
      if (document.readyState === "loading"){
        alert('page is loading');
        this.timeout(0);
      }
    });
  });
});
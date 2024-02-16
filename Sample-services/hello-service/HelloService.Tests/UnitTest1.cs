using HelloService.Controllers;
using Microsoft.AspNetCore.Mvc;
using NUnit.Framework;

namespace HelloService.Tests.Controllers
{
    public class HelloControllerTests
    {
        [Test]
        public void Get_ReturnsHello()
        {
            // Arrange
            var controller = new HelloController();

            // Act
            IActionResult result = controller.Get();

            // Assert
            Assert.IsNotNull(result);
            var okResult = result as OkObjectResult;
            Assert.IsNotNull(okResult);
            Assert.AreEqual("hello", okResult.Value);
        }
    }
}
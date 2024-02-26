using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace WorldService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WorldController : ControllerBase
    {
        private readonly ILogger<WorldController> _logger;
        private readonly IConfiguration _configuration;

        public WorldController(ILogger<WorldController> logger, IConfiguration configuration)
        {
            _logger = logger;
            _configuration = configuration;
        }

        [HttpGet]
        public IActionResult Get()
        {
            bool isWorldFeatureEnabled = _configuration.GetValue<bool>("FeatureFlags:WorldFeatureEnabled");

            _logger.LogInformation($"World feature enabled: {isWorldFeatureEnabled}");

            if (isWorldFeatureEnabled)
            {
                return Ok("World");
            }
            else
            {
                return NotFound(); // or any appropriate response for when the feature is disabled
            }
        }
    }
}

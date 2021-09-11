function k = wavenumber3(w, h)
%
% Function to calculate wavenumber k for given wave frequency w and water
% depth h, by Newton's method.
%
% Set h < 0 for deep water limit.
%

g = 9.80665;

k_deep = w.^2 / g;

if h < 0
    k = k_deep;
else
    k = zeros(size(w));
    alpha = k_deep * h;
    for i = 1:numel(w)
        z1 = alpha(i); % first guess
        z0 = 0;
        while abs(z1 - z0) > 1e-9
            z0 = z1;
            z1 = z0 - (z0 * tanh(z0) - alpha(i)) / (tanh(z0) + z0 * sech(z0).^2);
        end
        k(i) = z1/h;
    end
end
